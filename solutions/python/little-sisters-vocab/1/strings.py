"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended."""
    prefix = vocab_words[0]
    words = vocab_words[1:]
    
    # Create list with prefix first
    result = [prefix]
    
    # Add prefixed words
    for word in words:
        result.append(prefix + word)
    
    # Join with ' :: '
    return " :: ".join(result)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    if word.endswith("ness"):
        base = word[:-4]  # remove 'ness'
        
        # If word ends with 'i', change back to 'y'
        if base.endswith("i"):
            base = base[:-1] + "y"
            
        return base
    
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    
    # Remove punctuation from the selected word
    word = words[index].strip(".,!?")
    
    # Add 'en' to convert adjective to verb
    return word + "en"