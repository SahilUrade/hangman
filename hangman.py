from words import words
import string
import random


def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    lives = 7   # every wrong guess costs user one life
    unique_letters = set(word)  # letters in the word
    alphabets = string.ascii_lowercase
    used_letters = []   # what user has guessed so far

    while lives > 0 and len(unique_letters) > 0:
        print(f"You have {lives} lives left. You have used these letters: ", *used_letters)

        current_word = [letter if letter not in unique_letters else "_" for letter in word]
        print(f"You have guessed: ", *current_word)

        guess = input("Guess a letter: ")
        if guess not in alphabets:
            print("Make a valid guess!")
            lives -= 1
        elif guess in used_letters:
            print(f"You have already guessed {guess}.")
            lives -= 1
        elif guess in unique_letters:
            used_letters.append(guess)
            unique_letters.remove(guess)
        else:
            lives -= 1
            used_letters.append(guess)
            print("That letter is not in word!")
        if lives == 0:
            print(f"Sorry, you are dead! The word was: {word}")
        print("\n")

    if len(unique_letters) == 0:
        print(f"Congratulations, you correctly guessed the word: {word}!")


hangman()
