import os

my_path = input("Enter path: ")

if os.path.exists(my_path):
    print(f"This path: {my_path} exist")
    
    if os.access(my_path, os.R_OK):
        print("Readability")
    else:
        print("Not readability")
    
    if os.access(my_path, os.W_OK):
        print("Writability")
    else:
        print("Not writability")
        
    if os.access(my_path, os.X_OK):
        print("Executabibility")
    else:
        print("Not execitability")
    
else:
    print("Not exist such path")