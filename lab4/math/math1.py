from math import pi

def to_radian(degree: float):
    return pi/180 * degree

degree = float(input("Input degree: "))

print("Radian:",to_radian(degree))