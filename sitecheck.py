from urllib.request import urlopen
from re import fullmatch
import sys

if len(sys.argv) != 2:
    exit("Usage: python site-check.py url")
else:
    url = sys.argv[1]

if fullmatch(r'^http(s)?://(www.)?\w+\.\w+$', url):
    response = urlopen(url).getcode()
    if response == 200:
        print(f"Connected to {url} succesfully.")
    else:
        print(f"Failed to connect to {url}.")
    print(f"The response code was {response}.")
else:
    print("Invalid url.")
