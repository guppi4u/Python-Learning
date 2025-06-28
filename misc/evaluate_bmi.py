# Evaluate BIM program 

def bmi_cal(weight,height):
    #checking on weight and height values
    if weight < 20 or weight > 200 or \
        height < 1.0 or height >5.0:
        return None
    
    return (weight/height ** 2)
    

print(bmi_cal(10,6.0))
print()
print(bmi_cal(25,2.0))
print()
print(bmi_cal(52.5, 1.65))