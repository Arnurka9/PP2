
def squareNums(endPoint: int):
    for i in range(1, endPoint + 1):
        yield i**2

endPoint = int(input("Input end num: "))

for i in squareNums(endPoint):
    print(i)
