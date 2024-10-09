# Iterating over dict


def main():
    months = {"Jan": "January", "Feb": "February",
              "Mar": "March", "Apr": "Apirl"}

    # normal for loop iteration
    for month in months:
        print(month + ":"+months[month])

    print("*********************************")
    # iterating over items()

    for month, months in months.items():
        print(f"{month}:{months}")

    print("*********************************")

    # checking in operator , this will return boolean vlaue

    print("Sep" in months)


main()
