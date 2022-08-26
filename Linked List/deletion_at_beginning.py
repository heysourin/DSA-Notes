class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    def traversal(self):
        if self.head is None:
            print('Empty list')
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next


    def insertion_at_beginning(self, data):
        ib = Node(data)
        ib.next = self.head
        self.head = ib

    def insertion_at_end(self, data):
        ine = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ine

    def insertion_at_any_position(self, data, position):
        inp = Node(data)
        a = self.head
        for i in range(1, position-1):
            a = a.next
        inp.next = a.next
        a.next = inp

    def deletion_at_the_begining(self):
        a = self.head #assigning self.head 
        self.head = a.next #making the next node 'head'
        a.next = None #disconnecting the first node


        

n1 = Node(5)
sll = Sll()
sll.head = n1

n2 = Node(10)
n1.next = n2

n3 = Node(20)
n2.next = n3

n4 = Node(25)
n3.next = n4

sll.insertion_at_beginning(0)
sll.insertion_at_end(30)
sll.insertion_at_any_position(15,4)
sll.deletion_at_the_begining()
sll.traversal()
