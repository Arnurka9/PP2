import time
import math

num = int(input("Enter int: "))
breaktime = int(input("Enter milliseconds: "))

time.sleep(breaktime/1000) #now milliseconds

print("Sqeare root of int:", math.sqrt(num))
