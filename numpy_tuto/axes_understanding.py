
# Understanding Axes
'''
a two-dimensional array has a vertical axis (axis 0) and a horizontal axis (axis 1).

'''

import numpy as np

def axes_understanding():

# creating a 2D array
    table = np.array([
       [5, 3, 7, 1],
       [2, 6, 7 ,9],
       [1, 1, 1, 1],
       [4, 3, 2, 0],
    ])
    print("Original array:\n", table)

    # printing the shape of the array
    print("Shape of the array:", table.shape)

    # pringting max value in table
    print("Max value in the array:", np.max(table))

    # printing the min value in table
    print("Min value in the array:", np.min(table))
    
    # printing the max value in the first axis (axis 0)
    
    print("Max value in the first axis (axis 0):", np.max(table, axis=0))

    # printing the min value in the first axis (axis 0)
    print("Min value in the first axis (axis 0):", np.min(table, axis=0))

    # printing the max value in the second axis (axis 1)
    print("Max value in the second axis (axis 1):", np.max(table, axis=1))      

    # printing the min value in the second axis (axis 1)
    print("Min value in the second axis (axis 1):", np.min(table, axis=1))

    




if __name__ == "__main__":
    # calling the function
    axes_understanding()    


