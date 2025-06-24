
# Treating list as functional result

def create_list(n):
    #creating an emptylist 
    my_list=[]
    # iterating over list 
    for i in range(n):
        my_list.append(i)
    return my_list

# list starts with index zero
print(create_list(5))