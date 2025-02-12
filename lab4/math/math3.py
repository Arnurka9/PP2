from math import pi, tan

def area_regular_polygon(count_of_sides: int, lenght_of_side: float):
    return ((count_of_sides* lenght_of_side**2))/(4*tan(pi/count_of_sides))

count_of_sides = int(input("Input count of sides: "))
lenght_of_side = float(input("Input the length of a side: "))

area = area_regular_polygon(count_of_sides, lenght_of_side)

print(f"Area of regular polygon: {area:.4f}")