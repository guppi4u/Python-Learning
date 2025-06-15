'''
Your task is to write and test a function which takes two arguments (a year and a month)
 and returns the number of days for the given year-month pair (while only February is sensitive to the year value, 
 your function should be universal).
convince the function to return None if its arguments don't make sense.
'''

def days_in_month(year, month):
    # Validating input and type
    if not isinstance(year,int) or not isinstance(month,int):
        return None
    if month < 1 or month > 12 or year < 1:
        return None
    

    
    # Check for leap year
    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
        # Days in each month using sets 
    month_days = {
        1: 31,
        2: 29 if is_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_days[month]


print(days_in_month(2000,2))