
def area_parallelogram(base: float, height: float):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

print("Area of parallelogram", area_parallelogram(base, height))