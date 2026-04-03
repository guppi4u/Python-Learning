# List method practice 

def list_metds():
    spam=[5, 2, 8, 1, 9, 3, 7, 4, 6, 2]

    # find max and min 
    max_spam=max(spam)
    print(f'Max value in spam :{max_spam}')
    print("********************************")
    min_spam=min(spam)
    print(f'Min value in spam :{min_spam}')
    print("********************************")

    # count 
    count_repeate_spam=spam.count(2)
    print(f'No of 2s in spam list is :{count_repeate_spam}')
    print("********************************")

    # Removes all occurrences of 2
    value_to_remove =2
    update_spam_list=[x for x in spam if x !=value_to_remove]
    print(f'Updated list after removal of 2: {update_spam_list}')
    print("********************************")

    # Sorts the list in ascending order
    spam.sort()
    print(f'Sorted list : {spam}')
    print("********************************")

    # Reverses the sorted list
    spam.reverse()
    print(f'Reverse sort order list : {spam}')
    print("********************************")

    # Inserts the number 10 at position 3
    spam.insert(3,10)
    print(f'Updated spam list : {spam}')
    print("********************************")

    # Creates a copy of the list and clears the original
    spam_copy =spam.copy()
    spam.clear()
    print(f'Copied list from spam is : {spam_copy}')
    print("********************************")


list_metds()