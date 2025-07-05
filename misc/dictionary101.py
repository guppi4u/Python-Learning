
def create_dictionary():
    """
    Creates a dictionary with 101 common English words and their definitions.
    """
    dictionary = {
        "abandon": "to give up completely",
        "ability": "the power or skill to do something",
        "able": "having the power, skill, means, or opportunity to do something",
        "about": "on the subject of; concerning",
        "above": "at a higher level or layer than",
        # ... (add more words and definitions as needed)
        "zoo": "a place where animals are kept for public viewing"
    }
    
    return dictionary

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    
    # Example usage
    print("Dictionary contains:")
    for word, definition in my_dictionary.items():
        print(f"{word}: {definition}")
    
    # Check if a word is in the dictionary
    word_to_check = "ability"
    if word_to_check in my_dictionary:
        print(f"\n'{word_to_check}' is in the dictionary.")
    else:
        print(f"\n'{word_to_check}' is not in the dictionary.")

        
