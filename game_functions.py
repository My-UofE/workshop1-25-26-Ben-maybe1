import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = (poss_values[0] + poss_values[len(poss_values) - 1]) // 2
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if current_val < next_val and user_input == "h":
        return True
    elif current_val > next_val and user_input == "l":
        return True
    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    found = []
    for x in range(0,len(word)):
        if word[x] == letter:
            found.append(x)
    if len(found) == 0:
        print(f"Sorry, '{letter}' is not in the word")
        return False
    for x in range(0,len(found)):
        board[found[x]] = letter
    print(f"Well done! '{letter}' is in the word")
    return True
