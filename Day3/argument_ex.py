# Program whic accepts zero or more default, keyword and postional argument


def multiple_args(name, *args, **kwags):
    print(name)
    print()

    for arg in args:
        print(arg)

    print()

    for key in kwags:
        print(kwags, "=", kwags[key])


def main():
    multiple_args("Bob", 0, 1, 2, age=40, color="brown")


main()
