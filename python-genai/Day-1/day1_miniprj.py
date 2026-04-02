'''
Build a command-line application that collects and displays user information. 
This project combines all the concepts from 
Day 1: variables, data types, f-strings, user input, and operators. 
You'll create a simple but functional program that demonstrates your understanding of
Python's building blocks.
'''

def user_info_display():
    welcome_screen = f'''
    ╔════════════════════════════════════════╗
    ║   Welcome to User Info Collector!      ║ 
    ╚════════════════════════════════════════╝
    '''
    print(welcome_screen)  # Fixed: was printing string literal instead of variable
    
    # User input 
    print('Please provide the following information:\n')
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    age = int(input('Enter your birth year: '))
    email_add = input('Enter your email address: ')
    phone_num = input('Enter your phone number: ')
    residence = input('Enter your city of residence: ')
    no_of_prgm = int(input('Enter number of programs you know: '))
    favorite_prgm = input('Enter your favorite program name: ')
    no_years_coding = int(input('Enter number of years of coding experience: '))
    if_student = input('Are you student or not (yes or no): ')

    # Calculation 
    user_age = 2026 - age
    avg_prgm_learnt = round(no_of_prgm / user_age, 2)  # Fixed: added rounding for readability

    # Check experience level 
    def check_exp_level(years):
        if 0 < years < 1:
            return 'Beginner'
        elif 1 <= years < 3:
            return 'Intermediate'
        elif 3 <= years < 15:
            return 'Advanced'
        elif years >= 15:
            return 'Expert'
        else:
            return 'Unknown'

    exp_level = check_exp_level(no_years_coding)  # Fixed: capture return value

    # Display information in eye-pleasing format
    display_info = f'''
╔═══════════════════════════════════════════════════════════╗
║              USER INFORMATION SUMMARY                     ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Personal Information:                                    ║
║  ─────────────────────────────────────────────────────   ║
║  Full Name:        {fname} {lname:<40}║
║  Age:              {user_age} years old{'':<33}║
║  Birth Year:       {age}{'':<42}║
║  Email:            {email_add:<40}║
║  Phone:            {phone_num:<40}║
║  City:             {residence:<40}║
║  Student Status:   {if_student.capitalize():<40}║
║                                                           ║
║  Programming Experience:                                  ║
║  ─────────────────────────────────────────────────────   ║
║  Languages Known:  {no_of_prgm}{'':<42}║
║  Favorite Lang:    {favorite_prgm:<40}║
║  Years of Exp:     {no_years_coding} year(s){'':<36}║
║  Experience Level: {exp_level:<40}║
║  Avg Lang/Year:    {avg_prgm_learnt} languages per year{'':<24}║
║                                                           ║
║  ✓ Message: Keep up the great work!                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    '''
    print(display_info)

user_info_display()
