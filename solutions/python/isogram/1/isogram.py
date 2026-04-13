def is_isogram(string):
    seen = set()
    
    for char in string.lower():
        if char.isalpha():  # ignore spaces, hyphens, etc.
            if char in seen:
                return False
            seen.add(char)
    
    return True
