class Node:
    def __init__(self, data) :
        self.data=data
        self.previous :Node|None=None
        self.next :Node|None=None

class DoublyLinkedList:
    def __init__(self):
        self.head:Node|None=None
        self.tail:Node|None=None
        self.no_of_nodes=0

    def total_nodes(self):
        return self.no_of_nodes
    
    def insert_end(self, data):
        self.no_of_nodes+=1
        newNode=Node(data)
        if self.tail is None:
            self.head=self.tail=newNode
            
        else:
            newNode.previous=self.tail
            self.tail.next=newNode
            self.tail=newNode

    def traverse_forward(self):
        curr=self.head
        while curr is not None:
            print(curr.data,end= " ")
            curr=curr.next
        print()
    
    def traverse_backward(self):
        curr=self.tail
        while curr is not None:
            print(curr.data,end= " ")
            curr=curr.previous
        print()

if __name__=='__main__':
    ll=DoublyLinkedList()
    ll.insert_end(18)
    ll.insert_end('adam')
    ll.insert_end(7.5)
    ll.insert_end('roma')
    ll.traverse_forward()

    print('-'*23)
    ll.traverse_backward()