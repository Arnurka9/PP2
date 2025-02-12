
def sortEven(lastNum: int):
    for i in range(1, lastNum + 1):
        if i%2 == 0:
            yield i

lastNum = int(input("Input last num: "))

print(",".join(map(str, sortEven(lastNum))))