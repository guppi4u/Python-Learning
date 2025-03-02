# LAB 


# write a program that uses a for loop to "count mississippily" to five. Having counted to five,
# the program should print to the screen the final message "Ready or not, here I come!"
 
import time  # importing time package

# iterating over for loop and using range fucntion
for tick in range(6):
    print(f'{tick}, Mississippi') # each time loop iterate , printing tick value and word Mississipi
    time.sleep(1) # giving pause of 1 sec

print("Ready or not, here I come!") # printing final message