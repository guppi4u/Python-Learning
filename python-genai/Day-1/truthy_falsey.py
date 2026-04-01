
# checking truty and falsy values 

def checking_truthy_falsy_values():
    check_list=["0","1","","hello",[],[1,2,3],None,True,False,"False"]

    for i in check_list:
        if i:
            print(f'This value of {i} is Truthy')
        else:
            print(f'This value of {i} is Falsy')

checking_truthy_falsy_values()


