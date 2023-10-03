#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
test = -1 * number
dig = number % 10
if number < 0:
    dig = test % 10
    dig *= -1
if dig > 5:
    print(f"Last digit of {number} is {dig} and is greater than 5")
elif dig == 0:
    print(f"Last digit of {number} is {dig} and is {dig}")
else:
    print(f"Last digit of {number} is {dig} and is less than 6 and not 0")
