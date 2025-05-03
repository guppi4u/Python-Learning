'''
Then you take an arbitrary decision that the rows will record the 
readings every hour on the hour (so the row will have 24 elements)
 and each of the rows will be assigned to one day of the month
(let's assume that each month has 31 days, so you need 31 rows). 
 Here's the appropriate pair of comprehensions (h is for hour, d for day):

'''

def ListTempMatrix():

    temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.

    total = 0.0
    for day in temps:
        total += day[11]

    average = total / 31

    print("Average temperature at noon:", average)

#Now find the highest temperature during the whole month ‒ see the code:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)


# Now count the days when the temperature at noon was at least 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")




def main():
    ListTempMatrix()


main()