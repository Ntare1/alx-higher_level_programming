#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])

if (number < 0):
    digit = -digit

if (digit > 5):
    print(f'Last digit of {number} is {digit} and is greater than 5\n')
elif (digit) == 0:
    print(f'Last digit of {number} is {digit} and is 0\n')
elif  6 > (digit) and not 0:
    print(f'Last digit of {number} is {digit} and is less than 6 and not 0\n')

