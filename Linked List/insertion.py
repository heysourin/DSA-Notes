#? Insertion at the begining#Traversal in linkedlist

class Node:
    def __init__(self,data):
        self.data = data    #*  n1.data = 5 ,  n2.data = 10
        self.next = None    #*  n1.next = None, n2.next = None

class Sll:
    def __init__(self):
        self.head = None  #* sll.head = None
    
    def traversal(self):
        if self.head is None:
            print('Singly linkedlist is empty')
        else: #? else case is, when self.next is pointing to the next node we can do the traversal
            a = self.head #? assiging inside a as i dont want head value to change
            while a is not None:
                print(a.data, end =" ")
                a = a.next #? To connect one node to another


    def insert_at_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb



n1 = Node(5)

#creating object of Sll
sll = Sll()# creating object will make __init__ method run automatically
sll.head = n1


n2 = Node(10)
n1.next = n2

n3 = Node(15)
n2.next = n3

n4 = Node(20)
n3.next = n4

# sll.traversal()
sll.insert_at_begining(1)
sll.traversal()
