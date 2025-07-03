import numpy as np
def numpy_version():
    """
    Returns the version of the numpy library.
    
    Returns:
        str: The version of numpy.
    """
    return np.__version__

if __name__ == "__main__":
    print("Numpy version:", numpy_version())