# Title: Fibonacci Sequence
# Description: This program calculates the nth Fibonacci number using recursion and a closed form formula. This demonstrates the difference in time complexity between the two methods.
# Version: 10-21-2024

from cmath import sqrt
import time


def fib1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    result = (1 / sqrt(5)) * (((1 + sqrt(5))/2)**(n + 1) - ((1 - sqrt(5))/2)**(n + 1))
    return int(result.real) # Prevents small floating-point precision issues (ie. + 0j)

# Reading input as a string
while(True):
    userInput = input("Enter the nth Fibonacci Number in sequence to be generated. Type exit to exit program. ")
    if userInput == "exit":
        break
    elif not userInput.isdigit():
        print("Invalid input. Please enter a positive integer.")
        continue
    else:
        print(f"Generating the {userInput}th Fibonacci Number in sequence...")

        startTime = time.time()
        result1 = fib1(int(userInput))
        endTime = time.time()
        print(f"Using recursion: {result1} (Time: {endTime - startTime:.5f} seconds)")

        startTime = time.time() 
        result2 = fib2(int(userInput))
        endTime = time.time()
        print(f"Using closed form: {result2} (Time: {endTime - startTime:.5f} seconds)\n")
