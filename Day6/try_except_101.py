# Program for try catch


def greet():
    print("Hello World")
    print(1/0)


def main():

    try:
        greet()

    except:
        print("Something has gone worng")


main()
