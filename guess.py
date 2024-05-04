import random


def play():
    number = random.randrange(1, 100)
    while (guess := get_number()) != number:
        if guess < number:
            print("More")
        else:
            print("Less")
    print("You've got it.")


def get_number():
    return get_value("Type a number: ", int, limit(100))


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


def limit(limit_value):
    return lambda x: x in range(1, limit_value)


play()
