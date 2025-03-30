# creating beatles list program 

def beatles():

    #creating empty beatles list 
    beatles=[]
    
    #adding elements to list 
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")

    #printing list fo beatles
    print(beatles)

    # Step 3: Use a for loop and the append() method to prompt the user to add members of the band
    members_to_add = ["Stu Sutcliffe", "Pete Best"]

    #using for loop to iterate members_to_add list 
    for members in members_to_add:
        beatles.append(members)

    #printing updated beatles list 
    print(f'Updated beatles list: {beatles}')

    # Step 4: Use the del instruction to remove Stu Sutcliffe and Pete Best from the list
    del beatles[3]  # Remove Pete Best (index 3)
    del beatles[3]  # Remove Stu Sutcliffe (index 3 after Pete Best is removed)

        # Display the list after removal
    print("Beatles members after removal:", beatles)

    # Step 5: Use the insert() method to add Ringo Starr to the beginning of the list
    beatles.insert(0, "Ringo Starr")

    # Display the final list of Beatles members
    print("Final Beatles members:", beatles)

 

# creating main function
def main(): 
    beatles()


main()