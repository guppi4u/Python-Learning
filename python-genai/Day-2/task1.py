
# Conditional Logic 

def check_age_licence():
    user_age=int(input('Enter your age :'))
    has_license=input('Do you have license ? (yes/no)')

    if user_age > 0 and user_age < 13:
        print('Child')
    elif user_age > 13 and user_age < 19:
        if has_license =='yes':
            print('This is teen and also can drive')
        else:
            print('Teen ,without license')
    elif user_age > 20 and user_age < 64:
        if has_license =='yes':
            print('This is an adult and can drive')
        else:
            print('This is an adult with no license and cannot drive')
    elif user_age > 65 and has_license =='yes':
        print('This is an senior and can drive')
    else:
        print('This is an senior without license')



check_age_licence()
    
        
        
