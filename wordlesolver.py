import sys
import re
from collections import Counter

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [word.strip().lower() for word in file if len(word.strip()) == 5]

def filter_words(words, included, excluded, pattern):
    filtered = []
    for word in words:
        if (all(letter in word for letter in included) and
            all(letter not in word for letter in excluded) and
            re.match(pattern, word)):
            filtered.append(word)
    return filtered

def create_pattern(placement):
    return '^' + ''.join([letter if letter.isalpha() else '.' for letter in placement]) + '$'

def main():
    if len(sys.argv) != 4:
        print("Usage: python wordle_helper.py <included_letters> <excluded_letters> <letter_placement>")
        print("Example: python wordle_helper.py ae kpty a____")
        sys.exit(1)

    included = sys.argv[1].lower()
    excluded = sys.argv[2].lower()
    placement = sys.argv[3].lower()

    if len(placement) != 5 or not all(c.isalpha() or c == '_' for c in placement):
        print("Error: Letter placement must be 5 characters long and contain only letters or underscores.")
        sys.exit(1)

    words = load_dictionary("words.txt")
    pattern = create_pattern(placement)
    
    possible_words = filter_words(words, included, excluded, pattern)

    if not possible_words:
        print("No words found matching the given criteria.")
    else:
        print(f"Found {len(possible_words)} possible words:")
        for word in possible_words:
            print(word)

    if possible_words:
        letter_freq = Counter(''.join(possible_words))
        print("\nMost common letters in remaining words:")
        for letter, count in letter_freq.most_common(5):
            print(f"{letter}: {count}")

if __name__ == "__main__":
    main()
