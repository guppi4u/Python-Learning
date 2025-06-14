# python decorator with parameters 

def deco_with_args(func):
    def wrapper(*args,**kwargs):
        print(f'Arguments are :{args},{kwargs}')
        return func(*args,**kwargs)
    return wrapper


@deco_with_args
def add(a,b):
    return a + b

    
print(add(1,2))