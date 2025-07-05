
def my_function():
    my_tuple = (1, 10, 100)

    t1 = my_tuple + (1000, 10000)
    t2 = my_tuple * 3

    print(len(t2))
    print()
    print(t1)
    print()
    print(t2)
    print()
    print(10 in my_tuple)
    print()
    print(-10 not in my_tuple)

if __name__ == "__main__":
    my_function()
    # Output:
    # 9
    # (1, 10, 100, 1000, 10000)
    # (1, 10, 100, 1, 10, 100, 1, 10, 100)
    # True
    # True