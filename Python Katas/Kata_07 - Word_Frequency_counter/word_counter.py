
def count_word_frequencies(tect: str) -> dict:
    """Returns a dictionary with word counts"""
    
    from collections import Counter
    import string
    
    if not tect:
        raise ValueError("")
    
    rejects = "".join([sign for sign in string.punctuation if sign != "'"])
    
    new_text = "".join([letter for letter in tect if letter not in rejects])
    
    return dict(Counter(new_text.lower().strip().split()))

