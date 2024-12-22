# program for Json


from json import dump, load


def main():

    # creating data of different format
    numbers = [1, 2, 3, 4, 5.5, 70]
    text = "Hello Python"

    lookup = {1: "jan", 2: "feb", 3: "mar"}

    toSave = {"values": numbers,
              "greetings": text,
              "months": lookup
              }

    filename = "data.json"

    # writing json to a file

    with open(filename, 'wt') as file:
        dump(toSave, file)

    with open(filename, 'rt') as file:
        loaded = load(file)

    print(loaded)


main()
