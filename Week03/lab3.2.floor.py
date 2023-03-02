# labs3.2.floor.py
# Author: Orla Dowling
# floors a number
# create a program that takes in a float
# and ouputs a int rounded down
# this requires the math module math.floor()
# this in an inbuilt module 

import math

number_to_floor = float(input("Enter a float number: "))

floored_number = math.floor(number_to_floor)
absolute_value = abs(floored_number)

print('{} floored is {}'.format(number_to_floor,absolute_value))


