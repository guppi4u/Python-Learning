# Fridge Exercise

fridgeTempreture = int(input("Enter fridge tempreture:"))

if fridgeTempreture < 0:
    print("Fridge too Cold")
elif fridgeTempreture == 0 and fridgeTempreture < 4:
    print("Fridge OK")
elif fridgeTempreture > 4 and fridgeTempreture < 6:
    print("Fridge too warm")

else:
    print("Fridge is broken!!")


print("Fridge program is completed !!!")
