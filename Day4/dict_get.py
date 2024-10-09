# Program to get value from dict

def main():

    vehicals = {"honda": "Car",
                "bmw": "Car",
                "ducati": "Bike",
                "tata": "Truck"}

    print(vehicals)
    print(type(vehicals))

    print("****************************")

    # getting value from dict

    item = vehicals.get("Ashok")
    print(item)
    print(type(item))

    item2 = vehicals.get("honda")
    print(item2)


main()
