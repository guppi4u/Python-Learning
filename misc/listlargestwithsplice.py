
def Listlargestusingsplice():

    my_list = [17, 3, 11, 5, 1, 9, 7, 315, 13]
    largest = my_list[0]

    for i in my_list[1:]: # comparing only first element using splice operator 
        if i > largest:
            largest = i

    print(f'Largest number is :{largest}')


def main():
    Listlargestusingsplice()


main()