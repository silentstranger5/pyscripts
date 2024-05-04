import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def update(array, bars):
    for rec, val in zip(bars, array):
        rec.set_height(val)

def selection(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i, len(arr)):
            if arr[j] < arr[m]:
                m = j
        swap(arr, i, m)
        yield arr

def bubble(arr):
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                yield arr

def insertion(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            swap(arr, j, j + 1)
            j -= 1
            yield arr

def mergesort(arr, p, r):
    if p >= r:
        return

    q = (p + r) // 2
    yield from mergesort(arr, p, q)
    yield from mergesort(arr, q + 1, r)
    yield from merge(arr, p, q, r)
    yield arr

def merge(arr, p, q, r):
    b = arr[p:q+1].copy()
    c = arr[q+1:r+1].copy()
    b = np.append(b, np.inf)
    c = np.append(c, np.inf)
    i, j = 0, 0
    for k in range(p, r + 1):
        if b[i] <= c[j]:
            arr[k] = b[i]
            i += 1
            yield arr
        else:
            arr[k] = c[j]
            j += 1
            yield arr

def quicksort(arr, p, r):
    if p >= r:
        return

    q = p
    for u in range(p, r + 1):
        if arr[u] < arr[r]:
            swap(arr, q, u)
            q += 1
            yield arr
    swap(arr, q, r)
    yield arr
    yield from quicksort(arr, p, q - 1)
    yield from quicksort(arr, q + 1, r)    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("usage: python sort.py method")

    fig, ax = plt.subplots()
    arr = np.arange(1, 100)
    np.random.shuffle(arr)
    bars = ax.bar(range(len(arr)), arr)

    match sys.argv[1]:
        case "selection":
            algorithm = selection(arr)
        case "bubble":
            algorithm = bubble(arr)
        case "insertion":
            algorithm = insertion(arr)
        case "mergesort":
            algorithm = mergesort(arr, 0, len(arr) - 1)
        case "quicksort":
            algorithm = quicksort(arr, 0, len(arr) - 1)

    ani = animation.FuncAnimation(fig=fig, func=update, fargs=(bars,), frames=algorithm, interval=1, repeat=False)
    plt.show()
