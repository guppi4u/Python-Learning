# Creating user info display

def user_info():
    first_name=input('What is your first name ?\n')
    last_name=input('What is your last name ?\n')
    birth_year=int(input('What is your birth year (enter year) ?\n')) # type conversion from str to int
    favorite_number=int(input('What is your favorite number ?\n')) * 2
    
    user_age=2026-(birth_year)


    user_info_display=f'''
    =================== USER INFO =========================
    #  1. NAME :- {first_name}{last_name}               
    #  2. AGE :- {user_age}        
    #  3. FAVORITE NUMBER :- {favorite_number}                  
    ====================== END =============================
    '''
    print(user_info_display)


user_info()