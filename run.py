"""
Hangman
"""

# Install repository of available words
import random
from allwords import possible_words
import string


def generate_word(possible_words):
    """
    Will use the imported word list to select a word to be guessed in the game"
    """
    mystery_word = random.choice(possible_words)

    return(mystery_word)


def game():
    mystery_word = generate_word(possible_words)
    mystery_letters = set(mystery_word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    while len(mystery_letters) > 0
        user_guess = input("Enter a letter to check if it is in the mystery word.")
        if user_guess in alphabet - guessed_letters:
            guessed_letters.append(user_guess)
            if user_guess in mystery_letters:
                mystery_letters.remove(user_guess)

        elif user_guess in guessed_letters:
            print("You;ve already guessed that letter, please try again.")

        else: 
        print("Invalid character entered, please enter a leter from a to z.")

    


user_input = input("Type something:")
print(user_input)


#    if user_guess in alphabet - guessed_letters:
#    guessed_letters.add(user_guess)
#    if user_guess in mystery_letters:
#    mystery_letters.remove(user_guess)
#
#    elif user_guess in guessed_letters:
#    print("You have already guessed that letter, please make another guess.")
#    else:
#    print("You have entered an invalid character. Please guess a leter an unused leter A to Z.")


# Welcome user and ask for input of first name
# name_input = input("What is your name?")
# print(name_input)

# Use username to explain rules to user

# Ask user to press any key to begin

# Display word skeleton and empty gallowes, request first letter guess

# Run code to check if the input is valid - a single letter character from a to z

# Check whether guess is contained in word, if yes then congrat user, no add body part and comiserate

# If lives and letters remain, LOOP code

# If no lives remain then GAME OVER

# If no letters remain then CONGRATULATIONS

