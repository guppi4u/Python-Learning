# Creating bmi calculator which takes height(m) and weight(kg)


def bmi_cal(weight,height):
    return (weight/height**2) # weight /height * height


print(f"Calculated BMI value is :{bmi_cal(70,1.65)}")