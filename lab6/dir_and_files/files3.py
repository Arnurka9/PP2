import os

my_path = input("Enter path: ")

if os.path.exists(my_path):
    print(f"Yes, this path: {my_path} exist")
    
    print("File name:", os.path.basename(my_path))
    
    print("Directory name:", os.path.dirname(my_path))    
else:
    print("No, this path doesn't exist")