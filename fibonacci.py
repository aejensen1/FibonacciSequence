# Title: Fibonacci Sequence
# Description: This program calculates the nth Fibonacci number using recursion and a closed form formula.
# Version: 10-21-2024

from cmath import sqrt


def fib1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    result = (1 / sqrt(5)) * (((1 + sqrt(5))/2)**(n + 1) - ((1 - sqrt(5))/2)**(n + 1))
    return round(result.real) # Prevents small floating-point precision issues (ie. + 0j)

print("Using recursion: ", fib1(2))
print("Using closed form: ", fib2(2))

print("Using recursion: ", fib1(4))
print("Using closed form: ", fib2(4))

print("Using recursion: ", fib1(35))
print("Using closed form: ", fib2(35))