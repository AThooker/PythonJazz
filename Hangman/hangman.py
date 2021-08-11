import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_letters)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have", lives, ", You have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        #get user input
        user_letter = input("Guess a letter: ")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print("letter is not in the word")

        elif user_letter in used_letters:
            print("You already guessed that letter")
        else:
            print("I think you should google what a letter is boss")

    if lives == 0:
        print("Sorry you died")
    else:
        print("Yay you did it")


hangman()