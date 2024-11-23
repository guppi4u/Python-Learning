# program for python locating a module


import sys


def main():
    # this will print system path
    print(sys.path)
    print("******************")

    # iterating over dir path

    for dirs in sys.path:
        print(dirs)


main()
