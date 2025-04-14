import sys
import os
import psycopg2 

from functions import *

sys.path.append(os.path.abspath('..'))

from config import load_config

def main():
    config = load_config()
    conn = psycopg2.connect(**config)
    
    conn.autocommit = True #авто транзакции
    
    cursor = conn.cursor()
    
    sql = """CREATE TABLE IF NOT EXISTS contacts (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL UNIQUE,
                phone VARCHAR(20) NOT NULL UNIQUE
    );"""
    
    cursor.execute(sql)

    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from CSV")
        print("2. Insert from console or Update contact")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Select part of data")
        print("6. Insert many contacts")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            insert_data_csv('contacts.csv', cursor)
        elif choice == '2':
            insert_or_update(cursor)
        elif choice == '3':
            search_by_name_or_phone(cursor)
        elif choice == '4':
            del_by_name_or_phone(cursor)
        elif choice == '5':
            select_part_of_data(cursor)
        elif choice == '6':
            conn.notices.clear()
            insert_multiple_users(cursor, conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

    conn.close()
        

if __name__ == "__main__":
    main()