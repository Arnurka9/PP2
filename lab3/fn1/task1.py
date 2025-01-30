"""
A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
"""

def to_ounces(grams: float):
    ounces = 28.3495231 * grams
    return ounces


if __name__ == "__main__": #for import to another file
    grams = float(input("Grams: "))
    print("Ounces: ", to_ounces(grams))
