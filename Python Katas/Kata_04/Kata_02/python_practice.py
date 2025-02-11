def filter_numbers(num1, num2):
    """Create a Python program that returns all the numbers from 0-9 except for the 
    two numbers that the user has inputted.

    e.g. If a user inputs: 3 and 6

    The program will return: 1 2 4 5 7 8 9

    Args:
        num1 (int): The first number to exclude
        num2 (int): The second number to exclude
    """
    
    return [i for i in range(10) if i != num1 and i != num2]


def star_conversion(word, index):
    """Create a program that will turn the letter at the entered index into an asterisk.

    e.g.The given word: lovely
        The given index: 3

        The program must return: lo*ely

    Args:
        word (string): The word to be iterated 
        index (int): The index to be replaced
    """
    result =""
    for idx, letter in enumerate(word, start=1):
        if idx == index:
             result += "*"
        else:
            result += letter
    
    return result


def find_exponent(a, n):
    """Create a program to find an integer exponent x such that a^x = n.

    e.g. If user inputs: a=2 n=4

    The program will return: x=2

    Args:
        a (int): The base int
        n (_type_): The solution
    """
    

def reverse_cases(word_list):
    """Create a program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.

    Args:
        word_list (list): List to be reversed
    """


def month_days(month):
    """Create a program that returns the number of days in the month that the user inputs.

    e.g. If a user inputs: January

    The program will return: 31 days

    Args:
        month (str): month
    """


def remove_duplicates(list):
    """Create a program to remove duplicates from a list of integers, preserving order.

    Args:
        list (list): A list that will contain duplicate items.

    Input:
[1, 3, 4, 10, 4, 1, 43]
Output:
[1, 3, 4, 10, 43]
Input:
[10, 11, 13, 23, 11, 25, 23, 76, 99]
Output:
[10, 11, 13, 23, 25, 76, 99]    
    """


def fibonacci(n):
    """
    Create a program that returns a list, of n-length, of fibonacci numbers.

    e.g. For the argument n=4

    The program will return: 0 1 1 2

    Args:
        n (int): The expected list range
    """


def prime_words(sentence):
    """Create a program to find the string consisting of all the words whose lengths are prime numbers.

    Input:
The quick brown fox jumps over the lazy dog.
Output:
The quick brown fox jumps the
Input:
Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later.
Output:
Omicron Effect: Foreign Flights Won't On Dec 15,

    Args:
        sentence (str): _description_
    """

    
def shift_decimals(test_int, decimal_shift):
    """Create a program to shift the decimal digits n places to the left, wrapping the extra digits around. 
    If the shift > the number of digits in n, reverse the string.
Input:
n = 12345 and shift = 1
Output:
Result = 23451
Input:
n = 12345 and shift = 2
Output:
Result = 34512
Input:
n = 12345 and shift = 3
Output:
Result = 45123
Input:
n = 12345 and shift = 5
Output:
Result = 12345
Input:
n = 12345 and shift = 6
Output:
Result = 54321

    Args:
        test_int (int): int of 5 values
        decimal_shift (int): num of decimal shifts
    """

