# Creating prgm for checking logical operator 

def logical_operator():
    user_age=int(input('Enter your age :\n'))
    driving_licence=int(input("Do you have driving licence, answer in (1-yes/0-no) ?\n"))

    if user_age >= 18 and driving_licence == 1:
        print("They can drive")
    elif user_age >= 65 and driving_licence == 1:
        print("The are senior and they can drive")
    elif user_age >= 13 and user_age <= 20:
        print("The are teenagers")
    elif user_age >= 18:
        print("They can vote")


logical_operator()



