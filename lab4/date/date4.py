import datetime

date1 = datetime.datetime.strptime(input("Input date YYYY-MM-DD: "), "%Y-%m-%d")
date2 = datetime.datetime.strptime(input("Input another date YYYY-MM-DD: "), "%Y-%m-%d")

difference = (abs(date1 - date2)).total_seconds()

print("Difference in seconds:",difference)