# Program for catching error


def greet():
    print("Hello World")
    print(1/0)


def hello():
    d = dict()
    # trying to print a key in dic which does not exist
    print(d['hello'])


def main():

    try:
        greet()
        hello()

    except ZeroDivisionError:
        print("Its a divied by zero error")

    except KeyError:
        print("Its key error from dict")


main()
