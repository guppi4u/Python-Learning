# Program for next and iter

class Sequence:
    def __init__(self):
        self._values = ['A', 'B', 'C', 'D']

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        self._index += 1

        if self._index > len(self._values):
            raise StopIteration

        return self._values[self._index-1]


def main():
    s = Sequence()
    it = iter(s)

    print(it)

    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


main()
