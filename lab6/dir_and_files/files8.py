import os

file_path = input("Enter file path: ")

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("File successfully deleted!")
    else:
        print("It's a dictionary")
else:
    print("Not exist such path")