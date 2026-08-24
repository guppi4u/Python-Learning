
# Calculating standard deviation

import math

# in cms 
height = [140,145,135,150,130]

# cal average 

average_height = sum(height) /len(height)

print(f'Average height : {average_height}')


# Calculating squared differnce 

squared_difference = [(h - average_height) **2 for h in height]

print(f'Squared differnce : {squared_difference}')


# Calculating variance 

variance = sum(squared_difference) /len(squared_difference)

print(f'Variance : {variance}')

# calculating Sta dev which is square root of variance 

std_dev = math.sqrt(variance)

print(f'Standard deviation : {std_dev:.2f}')