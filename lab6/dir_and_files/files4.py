import os

my_path = input("Enter path: ")

if os.path.exists(my_path):
    
    if my_path.lower().endswith(".txt"):
        with open(my_path, "r", encoding="utf8") as textFile:
            amount_of_lines = sum(1 for _ in textFile)
            print("Amount of lines:", amount_of_lines)
            
    else:
        print("It's not a txt file")

else:
    print("Not exist such path")