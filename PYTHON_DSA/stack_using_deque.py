# Creating stack using deque (LIFO)


from collections import deque

# creating browser_history object 

browser_history=deque()

browser_history.appendleft('google.com')
browser_history.appendleft('yahoo.com')
browser_history.appendleft('msn.com')

print(f'Browser history as stack :{browser_history}')


# removing elements from stack 
browser_history.popleft()

browser_history.popleft()

print(f'Browser history after removing 2 elements from stack : {browser_history}')