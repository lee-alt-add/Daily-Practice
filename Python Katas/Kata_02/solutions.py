# todo.py

def calculate_average(numbers):
    """
    Calculate and return the average of a list of numbers.
    """

    return sum(numbers)/len(numbers)


def is_palindrome(s):
    """
    Check if a given string is a palindrome (ignoring spaces and case).
    """
    s = "".join(s.split())
    return s.lower() == s[::-1].lower()


def flatten_list(nested_list):
    """
    Flatten a nested list into a single list.
    """
    flattened = []
    
    def recursive_flatten(item):
        if isinstance(item, list):
            for subitem in item:
                recursive_flatten(subitem)
        else:
            flattened.append(item)
    
    recursive_flatten(nested_list)
    return flattened
                      


def word_count(text):
    """
    Count the occurrences of each word in a given text and return a dictionary.
    """
    text_as_list = text.split()
    
    return {k:text_as_list.count(k) for k in text_as_list}

print(word_count(""))


def find_common_elements(list1, list2):
    """
    Find and return the common elements between two lists.
    """
    pass
