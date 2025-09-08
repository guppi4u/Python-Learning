
# Creating own linked list 

# this represent head(starting point) in the list
from platform import node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# string represent of node 

    def __repr__(self):
        return str(self.data)
    



class Linkedlist:
    def __init__(self):
        self.head=None

    
    def __repr__(self):
        node = self.head
        nodes = [] # creating empty list called nodes 
        # iterating 
        while node is not None: # checking if node is not None
            nodes.append(node.data) # add it to nodes list
            node = node.next # keep node pointing to node.next
        nodes.append('None') # adding None at last
        return " --> " .join(nodes)
   






# creating object llist 

def testing_linkedlist():
    llist = Linkedlist()

    first_node = Node("a")
    llist.head = first_node
    print(llist)

    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node

    print(llist)


testing_linkedlist()