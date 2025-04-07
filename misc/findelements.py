# finding element in the list 

def ListElementFind():

        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # demo list 
        to_find = 5 # assiging variable for element which needs to be found
        found = False # setting boolen value as False for found

        for i in range(len(my_list)): # iterating over length of list 
            found = my_list[i] == to_find # if found mylist[i] will assign to find

            if found:
                break
        

        if found:
            print("Element found at index", i)
        else:
            print("absent")


def main():
     ListElementFind()



main()
     
