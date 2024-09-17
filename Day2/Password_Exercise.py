'''program which asks user to enter password and checks aganist hardcoded password.

if password is correct , it greets .

if password is worng it display Access Denied

program ask password for 3 times and exists
'''

PASSWORD = "Welcome123"


for i in range(3):
    userPassword = input("Enter your password:")
    if userPassword == PASSWORD:
        print("Welcome!!!")
        break

print("Access Denied")
print("Program Exit")
exit()
