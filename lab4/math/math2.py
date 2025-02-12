
def area_trapezoid(u_base: float, d_base: float, height: float):
    return (u_base + d_base)/2 * height

height = float(input("Height: " ))
u_base = float(input("Base, first value: " ))
d_base = float(input("Base, second value: " ))

print("Area of trapezoid:",area_trapezoid(u_base, d_base, height))
