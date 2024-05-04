import random


def get_dices(filename):
    try:
        f = open(filename, encoding='utf8')
    except OSError:
        exit("Invalid input file.")
    else:
        dices = f.read().rstrip('\n').split('\n')
    finally:
        if f in locals():
            f.close()
    
    dices = list('\n'.join(dices[5 * i : 5 * i + 5]) for i in range(6))
    first, second = tuple(random.randrange(6) for i in range(2))
    first, second = (dices[index] for index in (first, second))
    first, second = map(lambda x: x.split('\n'), (first, second))
    dices = '\n'.join(' '.join(items) for items in zip(first, second))
    return dices


print(get_dices('dices.txt'))
