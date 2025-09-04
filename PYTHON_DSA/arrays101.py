# Creating array data structures 
''''
Let us say your expense for every month are listed below,

    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190

'''


# creating list of monthly expense 

month_expenses=[2200,2350,2600,2130,2190]

print(month_expenses)

# 1. In Feb, how many dollars you spent extra compare to January?

print(f'Spent extra compare to January is :{month_expenses[1] - month_expenses[0]}')

# 2. Find out your total expense in first quarter (first three months) of the year.

print(f'Expenses for first 3 months is : {month_expenses[0]+month_expenses[1]+month_expenses[2]}')

# 3. Find out if you spent exactly 2000 dollars in any month

print(f'Did i spent exactly 2000$ in any of the given month ? : {2000 in month_expenses}')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

month_expenses.append(1980)
print(f'Updated monthly expense list : {month_expenses}')

''' 
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
month_expenses[3] =month_expenses[3]-200

print(f'April month updated monthly expense list : {month_expenses}')
