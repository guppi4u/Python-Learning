# Adding items to dict


def main():
    months = {"Jan": "January", "Feb": "February", "Mar": "March"}

    print(type(months))
    print(months)
    print("***************************************")

    # adding an itme to dict
    months['Apr'] = "April"
    print(months)

    print("***************************************")

    # adding another dict to a dict
    months.update({"May": "May", "Jun": "June", "Jul": "July"})
    print(months)


main()
