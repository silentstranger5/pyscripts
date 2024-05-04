import sys

def quadratic(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return 0
    else:
        return list((((-b - (d ** 0.5)) / 2), ((-b + (d ** 0.5)) / 2)))


if len(sys.argv) != 4:
    exit("usage: python quadratic.py a b c")
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
except ValueError:
    exit("coefficients must be integers")

roots = quadratic(a, b, c)
if not roots:
    exit("no solutions")
else:
    print(roots)