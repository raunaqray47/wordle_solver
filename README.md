# Wordle Solver

## Description

Wordle Solver is a Python script designed to assist players in solving Wordle puzzles. It filters a dictionary of words based on the information gathered from previous guesses in the game, helping narrow down possible solutions.

## Features

- Filters words based on known included and excluded letters
- Considers known letter placements
- Provides a list of possible words matching the given criteria
- Shows the most common letters in the remaining possible words

## Requirements

- Python 3.6 or higher
- A text file named `words.txt` containing a list of 5-letter words, one per line

## Usage

Run the script from the command line with the following syntax:

	python wordlesolver.py <included_letters> <excluded_letters> <letter_placement>


### Arguments:

1. `<included_letters>`: Letters known to be in the word (in any order)
2. `<excluded_letters>`: Letters known not to be in the word
3. `<letter_placement>`: Known letter placements, using underscores for unknown positions

### Example:

	python wordlesolver.py ae kpty a____


This example searches for words that:
- Include 'a' and 'e'
- Do not include 'k', 'p', 't', or 'y'
- Have 'a' as the first letter

## Output

The script will display:
1. The number of possible words found
2. A list of all possible words
3. The five most common letters in the remaining words

## Note

Ensure that the `words.txt` file is in the same directory as the script or provide the full path to the file in the `load_dictionary` function.

