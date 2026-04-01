
# creating a python script which stores personal info 

def display_user_info():
    FullName="Demo King"
    print(f'DataType of Fullname: {type(FullName)}')
    Age=34
    print(f'DataType of Age: {type(Age)}')
    Height =1.78
    print(f'DataType of Height: {type(Height)}')
    FavProgramLan="Python"
    print(f'DataType of FavProgramLan: {type(FavProgramLan)}')
    YearsOfCoding=19
    print(f'DataType of YearsOfCoding: {type(YearsOfCoding)}')
    CurrentPythonLearning=True
    print(f'DataType of CurrentPythonLearning: {type(CurrentPythonLearning)}')
   

    # Storing info in f-string in displaying in formatted way
    user_info=f'''
    ==== PERSONAL INFO ====

    1. Name:- {FullName}
    2. Age:- {Age}
    3. Height:- {Height}
    4. Favorite Programming Language:- {FavProgramLan}
    5. Years of Coding experience:- {YearsOfCoding}
    6. Are you learning Python:- {CurrentPythonLearning}

    ======== END ==========
    '''
    
    print(user_info)


display_user_info()