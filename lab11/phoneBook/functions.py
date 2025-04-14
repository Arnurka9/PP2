import csv

def insert_data_csv(csv_file, cursor):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['name']
            phone = row['phone']

            try:
                cursor.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                    (name, phone)
                )
                print(f"Inserted: {name} - {phone}")
            except:
                print("Error inserting")

def insert_or_update(cursor):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    
    sql = """
        CREATE OR REPLACE PROCEDURE insert_or_update(name_input VARCHAR(50), phone_input VARCHAR(20))
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM contacts WHERE name = name_input) THEN
                UPDATE contacts SET phone = phone_input WHERE name = name_input;
            ELSE 
                INSERT INTO contacts(name, phone) VALUES (name_input, phone_input);
            END IF;
        END;
        $$;
    """
    
    cursor.execute(sql)
    
    cursor.execute('CALL insert_or_update(%s, %s)', (name, phone))
    

def search_by_name_or_phone(cursor): #Function that returns all records based on a pattern
    name = input("Enter name/phone or part of name/phone: ")
    sql = """
        CREATE OR REPLACE FUNCTION search_users(pattern TEXT)
        RETURNS TABLE(user_id INT, name VARCHAR(50), phone VARCHAR(20))
        AS $$
        BEGIN
            RETURN QUERY
            SELECT contacts.id, contacts.name, contacts.phone
            FROM contacts 
            WHERE
                contacts.name ILIKE '%' || pattern || '%'
                OR contacts.phone ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
    """
    cursor.execute(sql)
    
    sql = "SELECT * FROM search_users(%s)"
    cursor.execute(sql, (name,))
    
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")


def select_part_of_data(cursor):
    sql = "SELECT COUNT(id) FROM contacts"
    cursor.execute(sql)
    len_of_table = cursor.fetchone()[0]
    print("Len of table is:", len_of_table)

    offset = int(input("Enter offset: "))
    if offset > len_of_table:
        print("Offset cannot be greater than length!")
        return 0
    elif offset < 0:
        print("Offset cannot be a negative!")
        return 0
    
    limit = int(input("Enter limit: "))
    if limit + offset > len_of_table:
        limit = len_of_table - offset
    elif limit < 0:
        print("Limit cannot be a negative!")
        return 0
    
    sql = """
        CREATE OR REPLACE FUNCTION select_offset_and_limit(offset_input INT, limit_input INT)
        RETURNS TABLE(user_id INT, name VARCHAR(50), phone VARCHAR(20))
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM contacts ORDER BY id LIMIT limit_input OFFSET offset_input;
        END;
        $$ LANGUAGE plpgsql;
    """
    
    cursor.execute(sql)
    cursor.execute("SELECT * FROM select_offset_and_limit(%s, %s)", (offset, limit))
    
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("The table is empty")

def del_by_name_or_phone(cursor):
    print("Del by name: 1")
    print("Del by phone: 2")
    choose = int(input("Choose: "))
    
    name = ""
    phone = ""
    
    if choose == 1:
        name = input("Enter name: ")
    elif choose == 2:
        phone = input("Enter phone: ")
    
    sql = """
        CREATE OR REPLACE PROCEDURE delete(name_input VARCHAR, phone_input VARCHAR, choose_input INT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF choose_input = 1 THEN
                DELETE FROM contacts WHERE name = name_input; 
            ELSE
                DELETE FROM contacts WHERE phone = phone_input;
            END IF;
        END;
        $$
    """

    cursor.execute(sql)
    
    cursor.execute('CALL delete(%s, %s, %s)', (name, phone, choose))


def insert_multiple_users(cursor, conn):
    names = list(map(str, input("Enter some names: ").split()))
    phones = list(map(str, input("Enter some phones: ").split()))
    
    sql = r"""
        CREATE OR REPLACE PROCEDURE insert_multiple_users(
        names_input VARCHAR(50)[], 
        phones_input VARCHAR(20)[]
        )
        LANGUAGE plpgsql
        AS $$
        DECLARE
            i INT;
            incorrect_data TEXT[] := '{}';
        BEGIN
            FOR i IN 1..ARRAY_LENGTH(names_input, 1) LOOP
                IF phones_input[i] !~ '^\d{10,20}$' THEN
                    incorrect_data := ARRAY_APPEND(incorrect_data, names_input[i] || ' - ' || phones_input[i]);
                ELSE
                    BEGIN
                        INSERT INTO contacts (name, phone)
                        VALUES (names_input[i], phones_input[i]);
                    EXCEPTION WHEN unique_violation THEN
                        RAISE NOTICE 'Skipping %', names_input[i];
                    END;
                END IF;
            END LOOP;

            RAISE NOTICE 'Incorrect data: %', incorrect_data; 
        END;
        $$;
    """
    
    cursor.execute(sql)
    cursor.execute("CALL insert_multiple_users(%s, %s)", (names, phones))
    
    if conn.notices:
        for notice in conn.notices:
            print(notice.strip())
        conn.notices.clear()
