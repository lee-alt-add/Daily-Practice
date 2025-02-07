# todo.py

def add_two_numbers(a, b):
    """
    Add two numbers and return their sum.
    """
    return a + b


def reverse_string(s):
    """
    Reverse a given string and return the reversed version.
    """
    return s[::-1]


def find_largest_number(numbers):
    """
    Find and return the largest number in a list of integers.
    """
    pass


def count_vowels(s):
    """
    Count and return the number of vowels in a given string.
    """
    alphabets = "aeiou"
    count = 0
    
    for letter in s:
        if letter.lower() in alphabets:
            count += 1
            
    return count


def fibonacci_sequence(n):
    """
    Generate and return the first n numbers in the Fibonacci sequence.
    """
    pass