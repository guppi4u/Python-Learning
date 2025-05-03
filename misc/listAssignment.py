'''
If you have a list list_1, then the following assignment: list_2 = list_1 does not make a copy of the list_1 list,
 but makes the variables list_1 and list_2 point to one and the same list in memory.
 
'''

def ListAssignment():
    # creating a list 

    vehicle_one=['car','bycycle','bus']

    print(f'Vehicale one content: {vehicle_one}')

    vehicle_two=vehicle_one # assignment operator

    del vehicle_one[0]

    print(vehicle_one)

    print("*********************")

    print(vehicle_two)


def main():
    ListAssignment()


main()
