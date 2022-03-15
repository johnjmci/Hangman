"""
Hangman
"""
# Install repository of available words
import random
# from allwords import possible_words
possible_words = ['apple', 'banana', 'pears']


# Welcome user and ask for input of first name
# name_input = input("What is your name?")
# print(name_input)

# Use username to explain rules to user

# Ask user to press any key to begin


wrong_answers = 0
guessed_letters = []
number_of_lives = 7
mystery_word = random.choice(possible_words)
mystery_letters = list(mystery_word)
wrong_letters = []

while wrong_answers < number_of_lives:
        print("Incorrect answers so far = ", end="")
        for letter in wrong_letters:
                print("{}, ".format(letter), end="")
        
        print("Lives remaining = : {}".format(number_of_lives - wrong_answers))
        user_guess = input("Enter a letter to check if it is in the mystery word.")

        while user_guess in guessed_letters or user_guess in wrong_letters:
                print("You've already guessed that letter, please try again.")
                user_guess = input("Enter a letter to check if it is in the mystery word.")

        if user_guess not in mystery_letters:
                wrong_answers += 1

                wrong_letters.append(user_guess)

        print("MYSTERY Word = ", end="")

        for letter in mystery_letters:
                if user_guess == mystery_letters:
                        guessed_letters.append(user_guess)
        
        for letter in mystery_letters:
                if letter in guessed_letters:
                        print(letter + " ", end="")
                else:
                        print(" _ ", end="")

        print(number_of_lives)

        if len(guessed_letters) == len(mystery_letters):
                print("You have won, well done!")
                break

if wrong_answers == number_of_lives:
        print("You have lost the game, why not try again")






"""
Will use the imported word list to select a word to be guessed in the game"
"""
#def generate_word(possible_words):
     

#def game():
 #   mystery_word = generate_word(possible_words)
  #  mystery_letters = set(mystery_word)
   # alphabet = set(string.ascii_uppercase)
    #guessed_letters = set()
#

# Display word skeleton and empty gallowes, request first letter guess
    
   



# isolate user input
#    user_guess = input("Enter a letter to check if it is in the mystery word.").upper()
# Check whether guess is contained in word, if yes then congrat user, no add body part and comiserate
# If lives and letters remain, LOOP code
# Run code to check if the input is valid - a single letter character from a to z
 ##   if user_guess in alphabet - guessed_letters:
   ##         guessed_letters.append(user_guess)
 ##   if user_guess in mystery_letters:
   ##         mystery_letters.remove(user_guess)

 ##   elif user_guess in guessed_letters:

  ##  else: 
   ##     print("Invalid character entered, please enter a leter from a to z.")


# If no lives remain then GAME OVER

# If no letters remain then CONGRATULATIONS

## game()
