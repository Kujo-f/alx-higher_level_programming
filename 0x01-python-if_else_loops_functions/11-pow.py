#!/usr/bin/python3

def pow(a, b):
    # Compute the value of a raised to the power of b
    result = 1  # Initialize result to 1
    for _ in range(b):  # Repeat b times
        result *= a  # Multiply result by a
    return result  # Return the final result
