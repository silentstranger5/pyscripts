import random
import string
import sys


def get_password(length):
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    weights = [4] * len(string.ascii_letters + string.digits) + [1] * len(string.punctuation) 
    password = list()
    for i in range(length):
        password.append(random.choices(characters, weights=weights)[0])
    random.shuffle(password)
    password = ''.join(password)
    return password


if len(sys.argv) == 2:
    try:
        length = int(sys.argv[1])
        if length < 1:
            raise ValueError
    except (IndexError, ValueError):
        exit("Usage: python password length")
else:
    length = 8

password = get_password(length)
print(password)
