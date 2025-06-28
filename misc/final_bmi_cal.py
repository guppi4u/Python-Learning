# Final BMI calculator

'''
what is the BMI of a person 5'7" tall and weighing 176 lbs?
'''


# importing other files
import ft_to_met
import pounds_to_kilo

# defining bmi functions


def bmi_calculator(weight, height):

    # input validation
    if height < 1.0 or height > 2.5 or \
            weight < 10 or weight > 200:
        return None
    return (weight/height ** 2)


# Calling other functions via dot operator

converted_weight = pounds_to_kilo.pounds_to_kilo(176)
converted_height = ft_to_met.feet_and_inch_to_meters(5, 7)




# Calculating BMI

print(f"Calculated BMI is: {bmi_calculator(converted_weight, converted_height)}")


