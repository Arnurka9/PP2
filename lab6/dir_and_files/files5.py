#writing part
var1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = ["Apple", "Banana", "Milk", True, False, 505, 404, 143, var1]

with open("txt_from_list.txt", "w", encoding="utf8") as text:
    text.write(str(lst))