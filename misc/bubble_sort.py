# Creating bubble sort program in python 

def BubbleSort():

    #creating list of numbers
    my_list = [8, 10, 6, 2, 4]

    swapped=True # a variable with boolean value 

    #Using while loop 

    while swapped:
        swapped=False # no swap till now 
        for i in range(len(my_list)-1): # list starts from zero index
            if my_list[i] >my_list[i+1]:
                swapped=True # swap occured 
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # re arranging the element in list 


    print(my_list)


def main():
    BubbleSort()


main()
