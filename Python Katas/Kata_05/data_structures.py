def create_person(name, surname, age):
    """
    Creates a dictionary representing a person with the given name, surname, and age.
    
    Args:
        name (str): The person's first name.
        surname (str): The person's last name.
        age (int): The person's age.

    Returns:
        dict: A dictionary with keys 'name', 'surname', and 'age'.
    """
    return {"name": name, "surname": surname, "age": age}

def update_age(person, new_age):
    """
    Updates the age of the given person in the dictionary.
    
    Args:
        person (dict): A dictionary representing a person.
        new_age (int): The new age to be set.
    
    Returns:
        None
    """
    person["age"] = new_age

def add_phone_number(person, phone_number):
    """
    Adds a phone number to the person's dictionary.
    
    Args:
        person (dict): A dictionary representing a person.
        phone_number (str): The phone number to be added.
    
    Returns:
        None
    """
    person["phone_number"] = phone_number

def remove_age(person):
    """
    Removes the 'age' key from the person's dictionary.
    
    Args:
        person (dict): A dictionary representing a person.
    
    Returns:
        None
    """
    del person["age"]

def display_person_info(person):
    """
    Displays the person's information (name, surname, age) in a formatted way.
    
    Args:
        person (dict): A dictionary representing a person.
    
    Returns:
        None
    """
    print(f"name: {person['name']}\nsurname: {person['surname']}\nage: {person['age']}")

def get_keys(person):
    """
    Retrieves all the keys from the person's dictionary.
    
    Args:
        person (dict): A dictionary representing a person.
    
    Returns:
        list: A list of keys in the person's dictionary.
    """
    return list(person.keys())

def get_values(person):
    """
    Retrieves all the values from the person's dictionary.
    
    Args:
        person (dict): A dictionary representing a person.
    
    Returns:
        list: A list of values in the person's dictionary.
    """
    return list(person.values())

def create_coordinates(x, y):
    """
    Creates a tuple representing coordinates (x, y).
    
    Args:
        x (int, float): The x-coordinate.
        y (int, float): The y-coordinate.
    
    Returns:
        tuple: A tuple containing the x and y coordinates.
    """
    return x, y

def append_to_list(lst, element):
    """
    Appends an element to the provided list.
    
    Args:
        lst (list): The list to which the element will be appended.
        element: The element to be added to the list.
    
    Returns:
        list: The updated list with the new element added.
    """
    lst.append(element)
    return lst

def add_to_set(s, element):
    """
    Adds an element to the provided set.
    
    Args:
        s (set): The set to which the element will be added.
        element: The element to be added to the set.
    
    Returns:
        set: The updated set with the new element added.
    """
    s.add(element)
    return s

def process_data(data):
    """
    Processes the provided data (list of tuples) and returns a dictionary where 
    the keys are names and the values are sets of ages associated with each name.
    
    Args:
        data (list of tuples): A list of tuples, where each tuple contains a name and an age.
    
    Returns:
        dict: A dictionary where each key is a name and the value is a set of ages.
    """
    
    output = {k: set() for k,v in data}
    
    for k,v in data:
        output[k].add(v)
    
    return output

def get_element_at_index(lst, index):
    """
    Retrieves the element at the specified index in the list.
    
    Args:
        lst (list): The list from which the element will be retrieved.
        index (int): The index of the element to retrieve.
    
    Returns:
        The element at the specified index.
    
    Raises:
        IndexError: If the index is out of range.
    """
    if index > len(lst) - 1:
        raise IndexError("index out of range")
    
    for idx, item in enumerate(lst):
        if idx == index:
            return lst[idx]

def double_values(lst):
    """
    Doubles each value in the provided list.
    
    Args:
        lst (list): The list of values to be doubled.
    
    Returns:
        list: A new list with each value doubled.
    """
    
    return [num * 2 for num in lst]

def sum_2d_list(lst):
    """
    Sums all the numbers in a 2D list.
    
    Args:
        lst (list of lists): A 2D list of numbers.
    
    Returns:
        int: The sum of all numbers in the 2D list.
    """
    return sum([sum(item) for item in lst])

def find_max_2d_list(lst):
    """
    Finds the maximum number in a 2D list.
    
    Args:
        lst (list of lists): A 2D list of numbers.
    
    Returns:
        int: The maximum number found in the 2D list.
    """
    pass

def unique_values_from_2d_list(lst):
    """
    Retrieves all unique values from a 2D list.
    
    Args:
        lst (list of lists): A 2D list of numbers.
    
    Returns:
        list: A list of unique values from the 2D list.
    """
    pass
