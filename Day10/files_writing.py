# program to write to a file


def writing():
    with open("Day10/write_test.txt", 'w') as file:
        file.write("Hello\n")
        file.write("World\n")

    print("Writing completed !!!")


def main():
    writing()


main()
