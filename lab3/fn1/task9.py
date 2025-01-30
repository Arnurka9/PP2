"""
Write a function that computes the volume of a sphere given its radius.
"""

def findVolumeOfSphere(radius):
    return 4/3*PI*(radius**3)

PI = 3.14
radius = float(input("Input radius of sphere: "))
print(findVolumeOfSphere(radius))