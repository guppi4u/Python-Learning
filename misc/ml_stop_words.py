"""
Stop words are words 
"""

def stop_words():
    # Your stop words set
    STOP_WORDS = {"the", "a", "an", "is", "it", "in", "on", "at", "to", "and", "or", "of", "for", "with"}

    text = input('Enter your text here or exit to quit: ')

    if text.lower().strip() =="exit":
        print("Thanks !!!")
        return

    # cleaning the text 
    words = text.lower().split()

    # Filter out the stop words

    fitered_words  = [ word for word in words if word not in STOP_WORDS]

    print(f'Filtered words : {fitered_words}')


if __name__ == "__main__":
    stop_words()