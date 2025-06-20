class StringProcessor:
    def reverse_words_in_sentence(self, sentence: str) -> str:
        """
        Reverses each word in a given sentence string, while preserving the original order
        of the words and the spacing between them.

        - Words are defined as sequences of non-space characters.
        - Punctuation attached to a word should be considered part of that word and
          reversed along with it.
        - Multiple spaces between words should be preserved.
        - Leading and trailing spaces in the original sentence should also be preserved.

        Examples:
        - "Hello World" should become "olleH dlroW"
        - "Python is fun!" should become "nohtyP si !nuf"
        - "  leading spaces" should become "  gnidael secaps"
        - "trailing spaces  " should become "gniliart secaps  "
        - "Multiple   spaces" should become "elpitluM   secaps"
        - "a b c" should become "a b c" (single letter words)
        - "" (empty string) should become ""
        - "  " (only spaces) should become "  "
        """
        for word in sentence.split():
            sentence = sentence.replace(word, word[::-1])
        
        return sentence

class NumberCruncher:
    
    def process_numbers(self, numbers: list[int]) -> dict[str, int]:
        import math
        """
        Processes a list of integers to calculate the sum of all even numbers
        and the product of all odd numbers.

        - 0 is considered an even number.
        - If the list is empty or contains no even numbers, the sum of evens should be 0.
        - If the list is empty or contains no odd numbers, the product of odds should be 1
          (as 1 is the multiplicative identity).

        Returns:
            A dictionary with two keys:
            - "sum_of_evens": The sum of all even numbers in the list.
            - "product_of_odds": The product of all odd numbers in the list.

        Examples:
        - [1, 2, 3, 4, 5] should return {"sum_of_evens": 6, "product_of_odds": 15}
        - [2, 4, 6, 0] should return {"sum_of_evens": 12, "product_of_odds": 1}
        - [1, 3, 5] should return {"sum_of_evens": 0, "product_of_odds": 15}
        - [] (empty list) should return {"sum_of_evens": 0, "product_of_odds": 1}
        - [-2, -3, -4, 5] should return {"sum_of_evens": -6, "product_of_odds": -15}
        """
        even = [x for x in numbers if x % 2 == 0]
        odd = [x for x in numbers if x % 2 != 0]
        return {"sum_of_evens": sum(even) if len(even) != 0 else 0,
                 "product_of_odds": math.prod(odd) if len(odd) != 0 else 1}

class LogicValidator:
    def check_discount_eligibility(self, age: int, is_member: bool, has_coupon: bool) -> str:
        """
        Determines a customer's discount eligibility based on their age,
        membership status, and whether they have a coupon.
        The rules are applied in the following order of precedence:

        1. If the age is 65 or over, they get a "Senior Discount", regardless of
           membership or coupon status.
        2. Else if the age is under 18 (i.e., 0-17), they get a "Student Discount",
           regardless of membership or coupon status.
        3. Else (age is between 18 and 64 inclusive):
            a. If they are a member AND have a coupon, they get a "Member Coupon Discount".
            b. Else if they are a member (but no coupon), they get a "Member Discount".
            c. Else if they have a coupon (but not a member), they get a "Coupon Discount".
            d. Otherwise (neither a member nor possessing a coupon), they get "No Discount".

        Return the string representing the determined discount type.
        Assume age will be a non-negative integer.
        """
        return "Senior Discount" if age >= 65 else \
                "Student Discount" if 0 <= age < 18 else\
                "Member Coupon Discount" if 18 <= age < 65 and is_member and has_coupon else \
                "Member Discount" if 18 <= age < 65 and is_member and not has_coupon else \
                "Coupon Discount" if 18 <= age < 65 and not is_member and has_coupon else \
                "No Discount"

class PasswordValidatorTDD:
    # NOTE TO STUDENT: For this class, you must first write the unit tests in
    # test_assessment.py for the `is_valid_password` method *before*
    # implementing the method itself. This is a Test-Driven Development (TDD) exercise.

    def is_valid_password(self, password: str) -> bool:
        import string
        """
        Validates a password string based on the following criteria.
        All criteria must be met for the password to be considered valid.

        1. Length: Must be at least 8 characters long AND no more than 30 characters long.
        2. Uppercase: Must contain at least one uppercase letter (A-Z).
        3. Lowercase: Must contain at least one lowercase letter (a-z).
        4. Digit: Must contain at least one digit (0-9).
        5. Special Character: Must contain at least one special character from the
           following set: ! @ # $ % ^ & * ( ) - _ + =

        If all criteria are met, return True. Otherwise, return False.
        You should implement this method *after* writing comprehensive unit tests
        for it in the test_assessment.py file.
        """
        valid_chars = len(password) > 7
        has_upper = len([x for x in password if x.isupper()]) > 0
        has_lower = len([x for x in password if x.islower()]) > 0
        has_digit = len([x for x in password if x.isalnum()]) > 0
        has_special_char = len([x for x in password if x in string.punctuation]) > 0

        return  valid_chars and has_upper and has_lower and has_digit and has_special_char

pd = PasswordValidatorTDD()
print(pd.is_valid_password("caught_flaw"))