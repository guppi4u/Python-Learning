# opening file using "with" construct

def main():

    with open("Day10/mall_customers.csv") as file:

        # reading line

        lines = file.readlines()

        for line in lines:
            print(line, end="")


main()
