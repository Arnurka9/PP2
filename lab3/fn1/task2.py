"""
Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)
"""

def to_centigrade(fahrenheit: float):
    return (5/9) * (fahrenheit - 32)

if __name__ == "__main__": 
    F = float(input("Fahrenheit: "))
    print("Centigrade: ", to_centigrade(F))