
# Creating timing function for decorator demo 

import time 

def timer(func):
    def wrapper(*args,**kwargs):
        start =time.time()
        result=func(*args,*kwargs)
        end=time.time()
        print(f'{func.__name__} took {end-start:.4f} seconds')
        return result
    
    return wrapper

@timer
def slow_function():
    time.sleep(4)
    print('Done!!!')

slow_function()




    