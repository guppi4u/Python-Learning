
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))


"""
Here's how fun(25) is calculated:

fun(25) is called.

25 is not greater than 30, so it will return 25 + fun(28).

To figure that out, fun(28) is called.

28 is not greater than 30, so it will return 28 + fun(31).

Next, fun(31) is called.

31 is greater than 30. The function hits its base case and returns 3.

Now, the results are passed back up the chain:

The value of fun(31) is 3. This is returned to the fun(28) call, which calculates 28 + 3 = 31.

The value of fun(28) is 31. This is returned to the original fun(25) call, which calculates 25 + 31 = 56.

Finally, print(fun(25)) outputs the final result.

"""