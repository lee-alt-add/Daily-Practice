# todo.py

def remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving the original order.
    """
    result = []
    
    for letter in lst:
        if letter not in result:
            result.append(letter)
            
    return result


def longest_substring_without_repeating_chars(s):
    """
    Find the length of the longest substring without repeating characters.
    """
    # return sorted(list({k:s.count(k) for k in s}.items()))


def group_anagrams(words):
    """
    Group a list of words into anagrams.
    """
    result = []
    visited = set()
    
    for x in words:
        holder = []
        for y in words:
            if sorted(x) == sorted(y) and y not in visited:
                visited.add(y)
                holder.append(y)
        if holder:
            result.append(holder)

    return result


def is_valid_parentheses(s):
    """
    Check if the input string of parentheses is valid.
    """
    pass


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    """
    return sorted([item for item in list1+list2])