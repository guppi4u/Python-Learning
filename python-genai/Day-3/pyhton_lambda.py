# Python lambda functions 


squares = lambda x:x ** 2
result=squares(6)
print(result)

print("*" * 100)
# With Map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers)) 
print(squared)