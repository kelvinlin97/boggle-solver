def clean_word_set(filename):
    valid_words = []
    try:
        with open(filename, 'r') as file:
            for word in file:
                word = word.strip()
                if len(word) >= 3:
                    valid_words.append(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return valid_words

def validate_word(word):
    word_set = clean_word_set('words_alpha.txt')
    return word in word_set