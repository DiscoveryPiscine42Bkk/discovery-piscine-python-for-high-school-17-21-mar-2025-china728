#!/bin/python3
original_array = [2,8,9,48,8,22,-12,2]
new_array = [x + 2 for x in original_array if x > 5]
print(f"Original_array: {original_array}")
print(f"New_array: {new_array}")