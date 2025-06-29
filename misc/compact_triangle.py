# Checking if given sides makes triangle in compact way

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
    
    
    


print(f"The given input states that this is triangle ?: {is_a_triangle(1,1,1)}")
print()
print(f"The given input states that this is triangle ?: {is_a_triangle(1,1,6)}")
