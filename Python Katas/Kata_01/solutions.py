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
    
    # Initialize a variable with the first element in the list
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest


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
    fib = [0,1]
    
    # Handle an input of 1 or 0
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    for _ in range(3,n+1):
        fib.append(fib[-1]+fib[-2])
        
    return fib