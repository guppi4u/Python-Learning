'''
A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

The functions:

    are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
    take one argument (the value corresponding to their names)


Here is some information to help you:

    1 American mile = 1609.344 metres;
    1 American gallon = 3.785411784 litres. 

'''

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    #this will convert number of liters to gallon
    gallons = litres / 3.785411784
    # This converts 100 kilometers into miles:
    miles = 100 * 1000 / 1609.344
    # function tells returns you how many miles the car can go on 1 gallon of fuel
    return miles / gallons

def miles_gallon_to_liters_100km(miles):

    # This converts miles per gallon into 100 kilometers per gallon:
    # Convert miles to meters
    # Convert meters to kilometers
    # Divide by 100 to get 100km

    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    # This gives you litres per 100 km,
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

