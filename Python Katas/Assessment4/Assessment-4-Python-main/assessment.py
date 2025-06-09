def get_list_element_or_default(data_list: list, index: int, default_value=None):
    """
    Retrieves an element from a list at a specific index.
    If the index is out of bounds, it returns the default_value.

    Args:
        data_list (list): The list to retrieve an element from.
        index (int): The index of the element to retrieve.
        default_value (any, optional): The value to return if the index is out of bounds.
                                      Defaults to None.

    Returns:
        any: The element at the specified index, or default_value if index is invalid.

    Learning Outcomes: Basic data structures (lists), Functions, Problem-solving (handling edge cases).
    """
    # TODO: Implement this function
    pass


def count_value_occurrences(data_list:list, value_to_count: any)-> int:
    """
    Counts how many times a specific value appears in a list.

    Args:
        data_list (list): The list to search within.
        value_to_count (any): The value to count occurrences of.

    Returns:
        int: The number of times value_to_count appears in data_list.

    Learning Outcomes: Basic data structures (lists), Functions, Problem-solving (iteration, conditional).
    """
    # TODO: Implement this function
    pass


def create_student_record(name: str, student_id: str or int, courses: list) -> dict:
    """
    Creates a dictionary representing a student's record.

    Args:
        name (str): The student's name.
        student_id (str or int): The student's ID.
        courses (list of str): A list of courses the student is enrolled in.

    Returns:
        dict: A dictionary with keys 'name', 'id', and 'courses_enrolled',
              and their corresponding values.

    Learning Outcomes: Basic data structures (dictionaries, lists), Functions.
    """
    # TODO: Implement this function
    pass


def find_largest_number_in_list(numbers: list) -> int or float or None:
    """
    Finds the largest number in a list of numbers.

    Args:
        numbers (list of int/float): A list of numbers.

    Returns:
        int/float or None: The largest number in the list.
                           Returns None if the list is empty.

    Learning Outcomes: Basic data structures (lists), Functions, Problem-solving (iteration, comparison).
    """
    # TODO: Implement this function
    pass


def combine_string_list(string_elements: list, joiner_char=" ") -> str:
    """
    Combines a list of strings into a single string, with each element
    separated by the joiner_char.

    Args:
        string_elements (list of str): A list of strings to combine.
        joiner_char (str, optional): The character or string to place between
                                     elements. Defaults to a single space " ".

    Returns:
        str: The combined string. Returns an empty string if string_elements is empty.

    Learning Outcomes: Basic data structures (lists of strings), Functions, Problem-solving (string operations).
    """
    # TODO: Implement this function
    pass