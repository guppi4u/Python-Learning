'''
Problem: Two Sum 
Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.   


'''

from doctest import Example


def two_sum():
    user_values=[]

    nums = input("Enter the array of integers (comma separated): ")
    if  nums == "exit":
        print("Exiting the program.")
        return []
    target = int(input("Enter the target integer: "))
    user_values = nums.split(",")
    # Remove any leading/trailing whitespace and convert to integers as list comprehension
    user_values = [int(x.strip()) for x in user_values]  # Convert to integers
    # Create a dictionary to store the indices of the numbers
    num_to_index = {}
    # Iterate through the list of numbers and check for the complement
    for i, num in enumerate(user_values):
        # Calculate the complement
        
        #complement = target - num calculates what number we need to add to current number to reach the target

        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        # If the complement is not found, store the index of the current number in the dictionary
        num_to_index[num] = i
    return []  # Return an empty list if no solution is found   
result = two_sum()
if result:
    print("Indices of the two numbers that add up to the target:", result)
else:
    print("No two numbers add up to the target.")   

two_sum()