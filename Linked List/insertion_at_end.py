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

    def insert_at_end(self, data):
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne #? the last node of the loop will be the end node
        


n1 = Node(5)

sll = Sll()
sll.head = n1

n2 = Node(10)
n1.next = n2

n3 = Node(15)
n2.next = n3

n4 = Node(20)
n3.next = n4



sll.insert_at_end(25)


sll.traversal()
