
# Creating linked list from python collection module 

from collections import deque

# deque -double ended que

#printing empty queue
print(deque())

# creating string of queue

print(deque('abcde'))

# creating a dic que 

print(deque([{'one':'a'},{'two':'b'}]))


# creating linkedlist 

llist=deque("abcdef")

print(llist)

# appending 
llist.append('gh') # will get added right side of list 

print(llist)

print("************************")
# removing element 

llist.pop()

print(f'Updated list after pop: {llist}')

print("************************")


# Adding elements to left of deque

llist.appendleft('12')

print(llist)


print("************************")


# removing from left

llist.popleft()

print(f'Updated list after left pop :{llist}')