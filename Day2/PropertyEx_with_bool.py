""" Property exercise using boolean"""


user_student = input("Are you student (y/n) ?")
user_somke = input("Do you smoke (y/n) ?")
user_pet = input("Do you own a pet (y/n) ?")

if (user_student == "y" and user_somke == "n" and user_pet == "n"):
    print("Property avaiable for rent")

elif (user_student == "y" and user_somke == "y" or user_pet == "n"):
    print("Property avaiable for rent")
elif (user_student == "n" and user_somke == "y" and user_pet == "y"):
    print("Property avaiable not for rent")


print("Program finished !!!")
