# calling sorted function

def main():
    animals = ['dog', 'elephant', 'cat', 'rat', 'rabbit', 'ant']

    def order(item):
        return len(item)

    animals1 = sorted(animals, key=len)

    print(animals1)


main()
