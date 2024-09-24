# Program shows on how to pass multiple argument 


def comedy(**attributes):
    print(type(attributes))

    for prop in attributes:
        print(prop ,":",attributes[prop])

    print()

def main():
    comedy(name="test1", genre="comedy", duration=10)
    comedy(name="test2", genre="war", duration=20)
    comedy(name="test3", genre="romance", duration=30)
        



main()


