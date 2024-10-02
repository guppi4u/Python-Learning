# Program to remove items from the lists

def main():
    week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    print(type(week))
    print(week)
    print("**************************************************")

    # using remove function

    week.remove("Sat")
    print(week)

    print("**************************************************")

    # using pop function-pop function will return removed item

    week.pop(0)

    print(week)

    print("**************************************************")

    # using clear function

    week.clear()
    print(week)

    print("**************************************************")

    '''using del keyworld-del keyword deletes complete list , if we try to use print after that , it will throw error'''

    months = ["Jan", "Feb", "Mar", "Apr"]

    del months
    # print(months)


main()
