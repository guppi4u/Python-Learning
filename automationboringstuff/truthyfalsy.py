'''
1. creating prgm for truthy and falsy values 
2. '0000' or '' are consider as FALSE 
3. anything other than this is TRUE

'''

name =''

while not name:
    print('Enter your name')
    name=input('>')

print('How many guests are expected to come')
no_guest=input('>')
if no_guest:
    print('Do you have enough food for guests ???')
print('Thank you !!!')