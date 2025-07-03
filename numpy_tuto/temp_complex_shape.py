
# Creating array of complex tempreature data
import numpy as np

def temp_shape():
    # Createing tempreature data
    temperatures = np.array([
        29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
    12.6, 49.9, 38.6, 31.3, 9.2, 22.2])

    # print shape of the array
    print("Shape of the array:", temperatures.shape)

    # reshaping the array -passing new shape as a tuple
    reshaped_temperatures = temperatures.reshape((2, 2, 3))

    # print the reshaped array
    print("Reshaped array:\n", reshaped_temperatures)

    print()

    print()

    # creating np.swapaxes for swapping axes and understanding the shape
    swapped_temperatures = np.swapaxes(reshaped_temperatures, 1, 2)
    print("Swapped axes array:\n", swapped_temperatures)


if __name__ == "__main__":
    # calling the function
    temp_shape()    



