from libretranslatepy import LibreTranslateAPI
from random import choice
import readline


lt = LibreTranslateAPI("https://translate.terraprint.co/")


def read(filename):
    try:
        file = open("wordlist")
    except OSError:
        return None
    else:
        wordlist = file.read().splitlines()
        file.close()
        return wordlist


def function(wordlist):
    if not wordlist:
        return False

    while True:
        word = choice(wordlist)
        if not all(i.isalpha() or i == ' ' for i in word):
            return False
    
        translation = lt.translate(word, "en", "ru").lower().strip()
    
        try:
            guess = input(f"Translate word {word}: ").lower()
        except EOFError:
            return True
    
        if guess == translation:
            print("Correct.")
        else:
            print(f"Wrong. Correct translation: {translation}.")


if function(read("wordlist")):
    print("Goodbye")
else:
    print("Invalid input file")
