#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10
n_number = number * -1
n_digit = n_number % 10
if n_number > 0:
    if n_digit < 6 and n_digit != 0:
        print(f"Last digit of {number:d} is {-n_digit:d} and is less than 6 and not 0")
else:
    if l_digit > 5:
        print(f"Last digit of {number:d} is {l_digit:d} and is greater than 5")
    elif l_digit == 0:
        print(f"Last digit of {number:d} is {l_digit:d} and is 0")
    elif l_digit < 6:
        print(f"Last digit of {number:d} is {l_digit:d} and is less than 6 and not 0")
