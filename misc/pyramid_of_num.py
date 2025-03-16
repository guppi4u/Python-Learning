# this program calculates the height of a pyramid that can be built using a given number of blocks using top-down approach
def pyramid_height(blocks):
    height = 0  # To store the number of complete layers
    current_layer = 1  # Start with the first layer
    blocks_needed = 1  # First layer needs 1 block
    
    while blocks >= blocks_needed:  # Check if we can build the current layer
        height += 1  # We can build another layer
        blocks -= blocks_needed  # Subtract the blocks used for this layer
        current_layer += 1  # Move to the next layer
        blocks_needed = current_layer  # The next layer needs one more block than the previous layer
    
    return height

# Get user input for the number of blocks
blocks = int(input("Enter the number of blocks: "))  # Convert the input to an integer

# Call the function with the user input and store the result
result = pyramid_height(blocks)

# Print the result: height of the pyramid
print(f"Height of the pyramid: {result}")
