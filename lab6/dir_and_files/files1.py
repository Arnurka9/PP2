import os

my_path = input("Enter path: ")

if os.path.exists(my_path):
    directs = [d for d in os.listdir(my_path) if os.path.isdir(os.path.join(my_path, d))]
    files = [f for f in os.listdir(my_path) if os.path.isfile(os.path.join(my_path, f))]
    all_items = os.listdir(my_path)
else:
    print("Not exist such path")

print("Directories:", directs)
print("Files:", files)
print("All items:", all_items)