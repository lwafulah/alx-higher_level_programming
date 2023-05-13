#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

print(str.partition("object-oriented programming")[0] + "object-oriented programming")
