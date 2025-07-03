# Creating array of student grades and applying a curve

import numpy as np

# Create an array of student grades
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])

# creating a curve vriable
CURVE_CENTER = 80

# define a function to apply the curve


def apply_curve(grades):
    """
    Apply a curve to the grades based on the curve center.
    """
    # Calculate the average of the grades
    grades_average = np.mean(grades)

    print(f"Grades average: {grades_average}")

    # calculate the change from the curve center
    change = CURVE_CENTER - grades_average

    print(f"Change from curve center: {change}")

    # apply the curve to the grades
    # Vectorization is the process of performing the same operation 
    # in the same way for each element in an array
    # without using a loop.

    # Broadcasting is the process of extending two arrays of different
    # shapes and figuring out how to perform a vectorized calculation between them.
    #   In this case, we are adding the change to each element in the grades array.'''

    new_curved_grades = change + grades
    # Ensure that the new grades are within the range of 0 to 100
    print(f"New curved grades: {new_curved_grades}")

    # using clip function to ensure grades are between 0 and 100
    new_curved_grades = np.clip(new_curved_grades, grades, 100)

    print(f"New curved grades after clipping: {new_curved_grades}")
    # return the new curved grades
    return new_curved_grades


if __name__ == "__main__":

    # call the function to apply the curve
    apply_curve(grades)
