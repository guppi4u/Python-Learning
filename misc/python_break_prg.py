
# program to demo break statement with While


def breakPro():

    while True:
        user_input=input("Enter your input word\n")
        
        if user_input =="chupacabra":
            print("You've successfully left the loop.")
            
            break
    
    user_input=input("Enter your input word\n")

breakPro()