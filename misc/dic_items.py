
# Creating a dictionary to hold item names and  iterate through for loop using items() method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key, value in dictionary.items():
    print(key, "->", value) 


print("*********************************")

# modifiying the dictionary by adding a new item

dictionary["lion"] = "lion"

# iterating through the modified dictionary
for key, value in dictionary.items():
    print(key, "->", value)


# returing only keys from the dictionary
print("*********************************")

for key in dictionary.keys():
    print(f" Keys of dic :{key}")


print("*********************************")

# returning only values from the dictionary
for value in dictionary.values():
    print(f" Values of dic :{value}")


# adding new key-value pair to the dictionary
print("*********************************")  
dictionary["elephant"] = "éléphant" 
# iterating through the updated dictionary
for key, value in dictionary.items():
    print(key, "->", value) 

# removing an item from the dictionary
print("*********************************")
dictionary.pop("dog")
# iterating through the dictionary after removing an item
for key, value in dictionary.items():
    print(key, "->", value) 
