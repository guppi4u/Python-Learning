# program to open file

def main():

    # opening of files
    file = open(
        "Day10/company_data.csv")

    # reading lines

    lines = file.readlines()

    # iterating over lines

    for line in lines:
        print(line)

    # closing the file

    file.close()


main()
