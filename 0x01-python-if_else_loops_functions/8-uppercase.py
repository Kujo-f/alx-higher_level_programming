#!/usr/bin/python3

def uppercase(s):
    """Print a string in uppercase."""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
