import math

def count_items(items):
    # TODO: Return the number of items in the list
    return len(items)

def sum_numbers(numbers):
    # TODO: Return the sum of all numbers in the list
    return sum(numbers)

def find_largest(numbers):
    # TODO: Return the largest number in the list
    return max(numbers)

def count_even_numbers(numbers):
    # TODO: Return the count of even numbers in the list
    return len([num for num in numbers if num % 2 == 0])

def sum_digits(number):
    # TODO: Return the sum of digits in the given number
    return sum([int(num) for num in str(number)])

def count_vowels(string):
    # TODO: Return the count of vowels in the string (case-insensitive)
    return len([letter for letter in string if letter in "aeiouAEIOU"])

def multiply_list_elements(numbers):
    # TODO: Return the product of all elements in the list
    return math.prod(numbers)
    

def create_number_triangle(n):
    # TODO: Return a list of strings representing a number triangle
    # Example for n=3: ['1', '22', '333']
    return [str(num) * num for num in range(1, n+1)]


def fibonacci_sequence(n):
    # TODO: Return a list of first n Fibonacci numbers
    pass

def remove_vowels(string):
    # TODO: Return the string with all vowels removed
    return "".join([letter for letter in string if letter not in "aeiouAEIOU"])

def create_multiplication_table(n):
    # TODO: Return a 2D list representing multiplication table up to n
    pass


def count_character_frequency(string):
    # TODO: Return a dictionary with character frequencies
    return {k:string.count(k) for k in string}


def reverse_words(sentence):
    # TODO: Return the sentence with each word reversed
    return " ".join([word[::-1] for word in sentence.split()])

def spiral_matrix(n):
    # TODO: Return a 2D list representing a spiral matrix of size n x n
    pass

def pascal_triangle(n):
    # TODO: Return a list of lists representing Pascal's triangle up to n rows
    pass

def longest_common_subsequence(str1, str2):
    # TODO: Return the length of the longest common subsequence of str1 and str2
    pass


def count_inversions(arr):
    # TODO: Return the number of inversions in the array
    pass


def create_hollow_square(n):
    # TODO: Return a list of strings representing a hollow square of side n
    pass

                    

def create_diamond(n):
    # TODO: Return a list of strings representing a diamond shape
    pass


print(create_diamond(3))

def create_hourglass(n):
    # TODO: Return a list of strings representing an hourglass shape
    pass

def create_spiral_string(n):
    # TODO: Return a string spiraling from 1 to n^2 in a square pattern
    pass

def create_alphabet_diamond(n):
    # TODO: Return a list of strings representing a diamond using alphabets
    # Example for n=3: ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
    pass

def create_number_spiral(n):
    # TODO: Return a list of strings representing a spiral of numbers
    pass

def create_pyramid(n):
    # TODO: Return a list of strings representing a pyramid
    # Example for n=3: ['  *  ', ' *** ', '*****']
    pass

