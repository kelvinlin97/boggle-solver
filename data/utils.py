import os

def clean_word_set(filename):
    valid_words = []
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        with open(file_path, 'r') as file:
            for word in file:
                word = word.strip()
                if len(word) >= 3:
                    valid_words.append(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return valid_words

LATEST_WORD_SET = clean_word_set('words_alpha.txt')

def validate_word(word):
    return word in LATEST_WORD_SET