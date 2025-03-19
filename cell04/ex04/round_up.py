#!/bin/python3
import math
number = input("Give me a number: ")
number_float = float(number)
rounded_up = math.ceil(number_float)
print(int(rounded_up))