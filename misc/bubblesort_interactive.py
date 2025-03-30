def BubblesortInteractive():
    # Initialize an empty list to store user inputs
    my_list = []
    # Flag to track if a swap occurred during the iteration
    swapped = True

    # Prompt the user to input the number of elements they want to sort
    num = int(input("How many elements do you want to sort: "))

    # Collect the elements from the user
    for i in range(num):
        val = float(input("Enter a list element: "))  # Accepts float values for sorting
        my_list.append(val)  # Add the input value to the list

    # Perform the Bubble Sort algorithm
    while swapped:  # Continue sorting until no swaps are made
        swapped = False  # Reset the swapped flag at the start of each pass
        for i in range(len(my_list) - 1):  # Iterate through the list
            if my_list[i] > my_list[i + 1]:  # Compare adjacent elements
                # Swap the elements if they are in the wrong order
                swapped = True  # Set the flag to True since a swap occurred
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    # Print the sorted list
    print("\nSorted:")
    print(my_list)


# Call the function to execute the sorting
if __name__ == "__main__":
    BubblesortInteractive()

