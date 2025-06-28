def is_triangle_correct(a, b, c):
    # All three conditions must be TRUE for it to be a triangle
    # We also need to be strictly GREATER THAN, not just greater than or equal to,
    # unless you allow "degenerate" triangles (flat lines).
    # For a non-degenerate triangle, it must be > not >=
    
    # Condition 1: sum of two sides > third side
    cond1 = (a + b > c)
    # Condition 2:
    cond2 = (b + c > a)
    # Condition 3:
    cond3 = (c + a > b)

    # If ALL three conditions are True, then it's a triangle
    if cond1 and cond2 and cond3:
        return True
    else:
        return False

# A more concise way to write the same correct logic:
def is_triangle_concise(a, b, c):
    return (a + b > c) and \
           (b + c > a) and \
           (c + a > b)

print(is_triangle_concise(1,1,1)) # Expected: True
print(is_triangle_concise(1,1,3)) # Expected: False