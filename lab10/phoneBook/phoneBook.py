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
                name VARCHAR(50),
                phone VARCHAR(20) NOT NULL UNIQUE
    );"""
    
    cursor.execute(sql)

    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Search contact")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            insert_data_csv('contacts.csv', cursor)
        elif choice == '2':
            insert_data_input(cursor)
        elif choice == '3':
            update_data(cursor)
        elif choice == '4':
            search_by_name_or_phone(cursor)
        elif choice == '5':
            del_by_name_or_phone(cursor)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

    conn.close()
        

if __name__ == "__main__":
    main()