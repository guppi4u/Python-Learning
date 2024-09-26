# program to calculate BMI


def user_input():
    user_weight = int(input("Enter your weight :"))
    user_height = float(input("Enter your height :"))
    user_ht_mts = float(user_height*0.3048)
    bmi = float(user_weight/(user_height)*(user_ht_mts))
    rounded_bmi = round(bmi, 2)
    print("User BMI is : "+str(rounded_bmi))


def main():
    user_input()


main()
