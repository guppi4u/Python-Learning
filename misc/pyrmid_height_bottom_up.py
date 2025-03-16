# this program calculates the height of a pyramid that can be built using a given number of blocks using bottom-up approach
def pyramid_height(blocks):
    height = 0  # To store the number of complete layers
    current_layer = 1  # Start with the first layer
    total_blocks_needed = 0  # To track total blocks required for each layer
    
    # Find the maximum possible height (this could be more than needed)
    while (total_blocks_needed + current_layer) <= blocks:
        height += 1
        total_blocks_needed += current_layer
        current_layer += 1

    return height

# Get user input for the number of blocks
blocks = int(input("Enter the number of blocks: "))  # Convert the input to an integer

# Call the function with the user input and store the result
result = pyramid_height(blocks)

# Print the result: height of the pyramid
print(f"Height of the pyramid: {result}")
