# Creating list and tuple and checking for immutability

def main():
    # tuple
    fruits1 = ("apple", "mango", "banana")
    fruits2 = ("grapes", "pear", "chiko")

    # printing tuple fruits1 id before adding
    print("Id before addition:" + str(id(fruits1)))
    print("****************************************")
    # adding or conctenating 2 tuples
    fruits1 += fruits1
    print("****************************************")
    print(fruits1)

    # printing tuple fruits1 id after adding
    print("Id before addition:" + str(id(fruits1)))

    print("****************LISTS******************")

    animals1 = ["cow", "cat", "cattle"]
    animals2 = ["lion", "tiger", "cheeta"]

    # printing list  animals1 id before adding
    print("Id before addition:" + str(id(animals1)))

    print("****************************************")

    animals1 += animals2
    print(animals1)

    print("****************************************")

    # printing list  animals1 id after adding
    print("Id before addition:" + str(id(animals1)))


main()
