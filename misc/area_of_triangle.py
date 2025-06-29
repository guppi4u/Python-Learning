
# Calculating are of triangle
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# Calculating area of triangle with heron formula
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# validating triangle input values
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


area1=area_of_triangle(1., 1., 2. ** .5)
print(f'Area of triangle is :{area1:.2f}')
