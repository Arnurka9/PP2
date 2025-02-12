
def squares(first_num:int ,last_num: int):
    for i in range(first_num, last_num + 1):
        yield i ** 2

first_num = int(input("Input first num: "))
last_num = int(input("Input last num: "))

for i in squares(first_num, last_num):
    print(i)