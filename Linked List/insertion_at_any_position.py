class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Sll:
    # def __init__(self):
    #     self.head = None

    def traversal(self):
        if self.head is None:
            print('Empty list') 
        else:
            a = self.head
            while a is not None:
                print (a.data, end=" ")
                a = a.next

    def insert_at_begining(self, data):
        nb = Node(data) #? 'nb' is an object of the class 'Node'
        nb.next = self.head #? 'nb' node pointing towards existing first node
        self.head = nb #? making 'nb' first node


    def insert_at_end(self, data):
        ne = Node(data)
        a = self.head
        while a.next is not None: #? untill last node is available
            a = a.next
        a.next = ne #? the last node of the loop will be the end node
        

    def insertion_at_anyposition(self, data, position):
        npn = Node(data)
        a = self.head
        for i in range(1, position-1):
            a = a.next
        npn.next = a.next 
        a.next = npn


n1 = Node(5)

sll = Sll()
sll.head = n1

n2 = Node(10)
n1.next = n2

n3 = Node(20)
n2.next = n3

n4 = Node(25)
n3.next = n4


sll.insert_at_begining(0)
sll.insert_at_end(30)
sll.insertion_at_anyposition(15,4)

sll.traversal()
