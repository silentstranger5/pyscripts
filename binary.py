import random
import sys


def random_search(limit):
    items = sorted(random.choices(range(limit), k=limit))
    index = binary(items, item := random.randrange(limit), len(items) - 1)
    print(items)
    if index >= 0:
        print(f"Index of {item} is {index}.")   
    else:
        print(f"{item} is not in list.")


def binary(items, value, n):
    p = 0;
    q = n - 1;
    while p < q:
        r = (p + q) // 2
        if items[r] == value:
            return r
        elif items[r] < value:
            p = r + 1
        else:
            q = r - 1
    else:
        return -1


if len(sys.argv) != 2:
    limit = 100
else:
    try:
        limit = int(sys.argv[1])
        if limit < 1:
            raise ValueError
    except ValueError:
        exit("Usage: python binary limit")

random_search(limit)
