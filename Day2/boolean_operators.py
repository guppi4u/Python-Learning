# Program checks for boolean operators "and", "or" and "Not"

is_windy = True
is_raining = False

staying_inside = is_windy and is_raining
can_go_out = is_windy or is_raining

# and always evaluates to false if either of LHS and RHS are false
if (staying_inside):
    print("Cannot go outside: " + str(staying_inside))

# or always evaluates to True if either of LHS and RHS are True
elif (can_go_out):
    print("Can go outside: " + str(can_go_out))


print("Flipping boolen value with not operator:" + str(not is_windy))

print("Program ended!!!")
