# We know from school that the sum of two arbitrary sides has to be longer than the third side.

def is_triangle(a,b,c):
    if a+b >=c:
        return True
    if b+c >=a:
        return True
    if c+a >=b:
        return True
    return False

print(is_triangle(1,1,1))
print()
print(is_triangle(1,1,3))