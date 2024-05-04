import random, sys


def play():
    word = get_word("wordlist.txt")
    visible_word = "-" * len(word)
    word_letters = set(word)
    used_letters = set()
    tries = 10
    
    while len(word_letters) > 0 and tries > 0:
        print(visible_word)
        letter = get_letter()
    
        if letter in word_letters:
            word_letters.remove(letter)
            visible_word = get_visible_word(word, word_letters)
        elif letter in used_letters:
            print("Letter already used.")
        else:
            tries -= 1
    
        used_letters.add(letter)
    
    if len(word_letters) == 0:
        print("You won.")
    else:
        print("You lose.")
    print(f"Word was {word}.")


def get_word(filename):
    try:
        f = open(filename)
    except OSError:
        return None
    else:
        word = random.choice(f.read().splitlines())
        return word
    finally:
        if f in locals():
            f.close()


def get_letter():
    return get_value("Type a letter: ", to_lower, is_letter)


def get_value(prompt, transform=None, condition=None):
    while True:
        try:
            value = input(prompt)
            if transform:
                value = transform(value)
            if condition and not condition(value):
                raise ValueError
        except ValueError:
            print("Invalid value.")
            continue
        else:
            return value


def get_visible_word(word, word_letters):
    return ''.join(letter if letter not in word_letters else '-' for letter in word)


def to_lower(s):
    return s.lower()


def is_letter(s):
    return (s.isalpha() or s == ' ') and len(s) == 1

play()
