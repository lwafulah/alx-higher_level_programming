#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

# Check if number of arguments
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

# Get the arguments and operator
a, operator, b = sys.argv[1:]

# Check if operator is valid
if operator not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

# Cast the arguments to integers
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Invalid argument. Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

# Perform the operation
if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    result = div(a, b)

# Print the result
print("{} {} {} = {}".format(a, operator, b, result))
