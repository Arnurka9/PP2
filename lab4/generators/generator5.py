
def reverseOut(first_num: int):
    for i in range(first_num, -1, -1):
        yield i

firstNum = int(input("Input first num: "))

for i in reverseOut(firstNum):
    print(i)
