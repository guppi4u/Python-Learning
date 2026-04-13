# Lambda functions 


# this will doubles the number
doubles_num = lambda n:2 * n

print(f'Double numbers :{doubles_num(6)}')

print("*" * 50)
# checking if number is postive
checking_positive =lambda n : n > 0
print(f'Checing positive numbers : {checking_positive(3)}')
print("*" * 50)

# Use map() with lambda to convert [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f'Doubled numbers : {doubled}')
print("*" * 50)

# Use filter() with lambda to get only positive numbers from [-2, -1, 0, 1, 2, 3]
numbers =[-2, -1, 0, 1, 2, 3]

postive_num =list(filter(lambda x:x>0,numbers))
print(f'Positive number : {postive_num}')
print("*" * 50)

# Use sorted() with lambda to sort ["apple", "banana", "cherry"] by length

fruits=["apple", "banana", "cherry"]
sorted_fruits =list(sorted(fruits,key=lambda x :len(x)))

print(f'Sorted fruits : {sorted_fruits}')