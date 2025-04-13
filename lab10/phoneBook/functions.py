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

def insert_data_input(cursor):
    name_input =  input("Input name: ")
    phone_input = input("Input phone: ")
    sql = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
    cursor.execute(sql, (name_input, phone_input))
    
def update_data(cursor):
    print("1. Update only name")
    print("2. Update only phone")
    
    func = int(input("Choose: "))
    
    if func == 1:
        name_input = input("Input name: ")
        phone_input = input("Input phone: ")
        sql = "UPDATE contacts SET name = %s WHERE phone = %s"
        cursor.execute(sql, (name_input, phone_input))
        
    elif func == 2:
        new_phone_input = input("Input phone: ")
        current_phone_input = input("Input phone: ")
        sql = "UPDATE contacts SET name = %s WHERE phone = %s"
        cursor.execute(sql, new_phone_input, current_phone_input)

def search_by_name_or_phone(cursor):
    print("1. Search by name")
    print("2. Search by phone")
    print("3. Search by name and phone")
    
    func = int(input("Choose: "))
    
    if func == 1:
        name_input = input("Input name (you can write part of it if you want): ")
        cursor.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name_input}%",))
    
    elif func == 2:
        phone_input = input("Input phone (you can write part of it if you want): ")
        cursor.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"%{phone_input}%",))
    
    elif func == 3:
        name_input = input("Input name (you can write part of it if you want): ")
        phone_input = input("Input phone (you can write part of it if you want): ")
        cursor.execute(
            "SELECT * FROM contacts WHERE name ILIKE %s AND phone LIKE %s",
            (f"%{name_input}%", f"%{phone_input}%")
        )
    
    else:
        print("Invalid option")
        return

    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

    

def del_by_name_or_phone(cursor):
    print("1. Del by name")
    print("2. Del by phone")
    
    func = int(input("Choose: "))
    
    if func == 1:
        name_input = input("Input name: ")
        sql = "SELECT * FROM contacts WHERE name = %s"
        cursor.execute(sql, (name_input,))
        print(cursor.fetchall())
        person_id = int(input("Input id of person: "))
        sql = "DELETE FROM contacts WHERE name = %s AND id = %s"
        cursor.execute(sql, (name_input, person_id))
        
    elif func == 2:
        phone_input = input("Input phone: ")
        sql = "DELETE FROM contacts WHERE phone = %s"
        cursor.execute(sql, (phone_input,))
