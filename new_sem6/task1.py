from sys import argv
from guess_number import guess_number as g

# start, end, tries = 1, 100, 10
start, end, tries = (int(i) for i in argv[1:])

g(start, end, tries)