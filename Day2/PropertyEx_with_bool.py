""" Property exercise using boolean"""


user_student = input("Are you student (y/n) ?")
user_somke = input("Do you smoke (y/n) ?")
user_pet = input("Do you own a pet (y/n) ?")

if (user_student == "y" and user_somke == "n" and user_pet == "n"):
    print("Property avaiable for rent 1")

elif (user_student == "y" and user_somke == "y" or user_pet == "n"):
    print("Property avaiable for rent 2")

elif (user_student == "n" and user_somke == "y" and user_pet == "y"):
    print("Property not avaiable for rent")

elif (user_student == "y" and user_somke == "y" and user_pet == "y"):
    print("Property not avaiable for rent")


print("Program finished !!!")

# this program has logic problem , will upload updated one later
