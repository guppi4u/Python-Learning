# Program demonstrates calling multiple functions


def greetings():
    print("Welcome on board!!!")


def checking_password():
    PASSWORD = "Welcome123"

    user_input = input("Enter your password >")
    if user_input == PASSWORD:
        print("Access Granted")

    else:
        print("Access Denied!")


def main():
    greetings()
    checking_password()


main()
