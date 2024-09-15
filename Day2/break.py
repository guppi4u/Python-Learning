# Program for "break" keyoword


for i in range(5):
    print("Loop start:"+str(i))

    question = input("Stop loop or not ? (y/n)")

    if question == "y":
        break

    print("Ending loop")


print("Program finished!!!")
