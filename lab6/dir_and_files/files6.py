import os

folder = "files_as_letters"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

os.makedirs(folder, exist_ok=True)


for letter in letters:
    my_path = os.path.join(folder, f"{letter}.txt")
    
    with open(my_path, "w", encoding="utf8") as file:
        file.write("")