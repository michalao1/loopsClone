#!/usr/bin/python
# how is this?
import random

number = random.randint(1, 6)

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number}   Even number!")  # Prints a message if the number is even
else:
    print(f"{number}   Odd number!")  # Prints a message if the number is odd