#!/usr/bin/python3


def fizzbuzz():
    #Print numbers from 1 to 100 with FizzBuzz rules
    for num in range(1, 101):  # Loop from 1 to 100
        if num % 3 == 0 and num % 5 == 0:  # Check if num is divisible by both 3 and 5
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:  # Check if num is divisible by 3
            print("Fizz", end=" ")
        elif num % 5 == 0:  # Check if num is divisible by 5
            print("Buzz", end=" ")
        else:  # If none of the above conditions are met
            print(num, end=" ")
    print("")  # Print newline after all numbers are printed
