
def divisible_3_4(last_num: int):
    for i in range(1, last_num + 1):
        if i % 12 == 0:
            yield i
    

last_num = int(input("Input last num: "))

for i in divisible_3_4(last_num):
    print(i)
