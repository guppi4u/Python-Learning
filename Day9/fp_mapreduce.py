# Program objective taking set of random char and comparing with a word and printing matching words and rest with blank lines

from functools import reduce
from operator import add


def main():
    guesses = set('aeiou')
    word = 'facinate'

    result = reduce(add, map(lambda x: '-' if x not in guesses else x, word))

    print(result)


main()
