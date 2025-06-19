'''

Your task is to write and test a function which takes three arguments
 (a year, a month, and a day of the month) and returns the corresponding day of the year,
 or returns None if any of the arguments is invalid.

'''

# function 1 -Cheking if year is leap year or not 
def is_leap_year(year):
    return (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0)


# function 2 Checking days in month 

def days_in_month(year,month):
    if year <1582 and month < 1 and month >12:
        return None
    
    # Creating a list of days in each 12 months
    days_in_each_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month ==2 and is_leap_year(year):
        return 29
    return days_in_each_month[month-1] # python list starts with 0th index 


# function 3 checking number of days 

def day_of_year(year, month, day):
    total_days = 0
    
    # Add days from all previous months
    for m in range(1, month):
        dim = days_in_month(year, m)
        # If we get None, that means the month/year is invalid → so return None.
        if dim is None:
            return None
        # We add the number of days from each valid month to total_days.
        total_days += dim

    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None
    # Add the day of the current month
    return total_days + day

print(day_of_year(2024, 3, 15))  # Output: 75
