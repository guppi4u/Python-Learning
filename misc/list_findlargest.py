# this prog is finding larget number in list

def Listlargest():

    my_list = [17, 3, 11, 5, 1, 9, 37, 15, 13]  # defininig list

    largest = my_list[0]  # assuming 1st element in list is largest number

    for i in range(len(my_list)): # iterating over length of list 
        if my_list[i] > largest:   # checking if my_list[i]  item is greater than largets 
            largest = my_list[i]

    print(f'largest number is : {largest}')


def main():
    Listlargest()


main()
