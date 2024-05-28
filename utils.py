import os
import json
from typing import List

def clean_word_set(filename) -> List[str]:
    """
    Function accepts file path and parses valid words into a JSON file
    """
    valid_words = []
    try:
        input_file_path = os.path.join('data', 'input', filename)
        output_file_path = os.path.join('data', 'output', 'valid_words.json')
        
        with open(input_file_path, 'r') as file:
            for word in file:
                word = word.strip()
                if len(word) >= 3:
                    valid_words.append(word)
        with open(output_file_path, 'w') as output:
            json.dump(valid_words, output)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return valid_words
TARGET_FILE = 'words_alpha.txt'
LATEST_WORD_SET = clean_word_set(TARGET_FILE)

def validate_word(word: str):
    """
    Constant variables above are meant as placeholders for purpose of this project, function validates word by checking word bank
    """
    result = word in LATEST_WORD_SET
    return result

def validate_board(board):
    """
    Validate user submitted board
    """
    for row in board:
        for char in row:
            if not char.islower():
                return False
    return True

def generate_prefixes(word_set):
    """
    Generate a JSON file of prefixes from our most updated word list. 
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, 'data', 'output', 'prefixes.json')
    prefixes = set()
    
    for word in word_set:
        for i in range(len(word)):
            prefix = word[:i + 1]
            prefixes.add(prefix)

    prefixes_list = sorted(list(prefixes))
    try:
        with open(output_file_path, 'w') as file:
            json.dump(prefixes_list, file)
        print(f"File successfully written to {output_file_path}")
    except Exception as e:
        print(f"Error writing file: {e}")
    
    return prefixes

def load_data(filename):
    full_path = os.path.join('data', 'output', filename)
    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: JSON file '{filename}' not found at '{full_path}'")
    return data