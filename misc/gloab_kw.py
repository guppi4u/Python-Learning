
# Creating program for global keyword 

def my_function():
    global var 
    var = 2 
    print("Do i know that variable ?",var)

# Here variable name with global keyword takes precedence
var =1 
my_function()
print(var)