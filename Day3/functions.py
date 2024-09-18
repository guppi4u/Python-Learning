
'''Program to display function in python'''


def asking_user_status():
    checking = input("How are you feeling today ?")
    if checking == "OK" or checking == "ok":
        print("Awesome, good to hear that!!")
    else:
        print("Ho no.")


asking_user_status()
