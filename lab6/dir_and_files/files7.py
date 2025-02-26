import os 

file_1 = input("Enter txt full name or path: ")
file_name, file_ext = os.path.splitext(file_1)
file_2 = f"{file_name}_copy{file_ext}"

if os.path.isfile(file_1): #as a test for existence
    with open(file_1, "r", encoding="utf8") as file:
        text = file.read()
    
    with open(file_2, "w", encoding="utf8") as file:
        file.write(text)