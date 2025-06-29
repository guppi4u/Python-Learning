# Creating a right angle triangle 

# checking if given values makes triangle 
def is_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

# checking for right angle tirangle 
def is_a_right_triangle(a,b,c):
    if not is_triangle(a,b,c):
        return False
    
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    

print(is_a_right_triangle(5, 3, 4))
print()
print(is_a_right_triangle(1, 3, 4))

