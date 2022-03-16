import random
from allwords import possible_words
import string


# Use username to explain rules to user


# Welcome user and ask for input of first name
print('Welcome to Hangman!\nThis is a fun word game, where you guess the letters of a mystery word.')
print()
print('In this version of the game, all words have six letters.')
print()
username = input('Before we start, what should I call you? Plesae enter your first name... ').upper()
print()
print('Hi',username, '! Best of luck')
print()

input('Press any key to continue.')
print()

wrong_answers = 0
guessed_letters = []
number_of_lives = 7
alphabet = set(string.ascii_uppercase)
mystery_word = random.choice(possible_words)
mystery_letters = list(mystery_word)
wrong_letters = []


# Display word skeleton and empty gallowes, request first letter guess


while wrong_answers < number_of_lives:
        print('* Incorrect answers so far: ', end='')
        print()
        for letter in wrong_letters:
                print('{}, '.format(letter), end='')
        print('* Lives remaining: {}'.format(number_of_lives - wrong_answers))
        print()
        user_guess = input('--->>  Enter a letter to check if it is in the mystery word...').upper()



  # Run code to check if the input is valid - a single letter character from a to z

   ##     print("Invalid character entered, please enter a leter from a to z.")




        while user_guess in guessed_letters or user_guess in wrong_letters:
                print('You already made that guess, please try again')
                user_guess = input('--->>  Enter a letter to check if it is in the mystery word...').upper()

        if user_guess not in mystery_letters:
                wrong_answers += 1
                wrong_letters.append(user_guess)
        print()
        print('MYSTERY Word is ', end='')
        print()

        for letter in mystery_letters:
                if user_guess == letter:
                        guessed_letters.append(user_guess)
        
        for letter in mystery_letters:
                if letter in guessed_letters:
                        print(letter + ' ', end='')
                else:
                        print('_ ', end='')


        print()
        

        # If no lives remain then GAME OVER

# If no letters remain then CONGRATULATIONS

        if len(guessed_letters) == len(mystery_letters):
                print("You have won, well done!")
                break

if wrong_answers == number_of_lives:
        print("You have lost the game, why not try again")




