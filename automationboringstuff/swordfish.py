# swordfish prog 

'''
ALGO
1. ENTER INTO WHILE LOOP
2. LOOP THROUGH UNTILL NAME MTACHES 
3. ENTER PASSWORD AND EXIT 

'''
while True:
    print('Enter your name')
    name =input('>')
    if name !='Joe':
        continue
    print('Hello Joe , please enter your password')
    password =input('>')
    if password =='swordfish':
        break
print('Access granted!!!')
