"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:
"""

def histogram(sequence_nums: list):
    for num in sequence_nums:
        print("*" * num)


if __name__ == "__main__":
    sequence_nums = list(map(int, input("Input some ints: ").split()))
    histogram(sequence_nums)