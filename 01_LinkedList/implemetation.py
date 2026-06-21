from __future__ import annotations

class Node:
    def __init__(self, data):
        self.data=data
        self.next_node: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node |None =None
        self.no_of_nodes=0

    def size_of_list(self):
        return self.no_of_nodes
    
    #0(1) constant time
    def insert_start(self,data):
        self.no_of_nodes+=1
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next_node=self.head
            self.head=newNode


    def insert_end(self,data):
        self.no_of_nodes+=1
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next_node is not None:
                curr=curr.next_node
            curr.next_node=newNode

    #O(n)
    def remove(self,data):
        if self.head is None:
            return 
        curr=self.head
        prev: Node | None=None
        while curr is not None and curr.data!=data:
            prev=curr
            curr=curr.next_node
        
        if curr is None:
            return
        if prev is None:
            self.head=curr.next_node
        else:
            prev.next_node=curr.next_node

    def get_middle_node(self):
        # your implementation goes here !!!
        if self.head is None:
            return None
        if self.head.next_node is None:
            return self.head
        fast=slow=self.head
        while fast.next_node and fast.next_node.next_node is not None:
            slow=slow.next_node
            fast=fast.next_node.next_node
        return slow
    
    def reverse(self):
        if self.head is None:
            return None
        if self.head.next_node is None:
            return self.head
        prev=next=None
        curr=self.head
        while curr is not None:
            next=curr.next_node
            curr.next_node=prev
            prev=curr
            curr=next
        self.head=prev

    def traverse(self):
        if self.head is None:
            return
        curr=self.head
        while curr is not None:
            print(curr.data,end= '->')
            curr=curr.next_node
        print()

if __name__=='__main__':
    ll=LinkedList()
    ll.insert_end(18)
    ll.insert_start('adam')
    ll.insert_start(7.5)
    ll.insert_end('roma')
    ll.traverse()

    print('-'*23)
    # ll.remove('adam')
    ll.insert_end('goog')
    ll.traverse()


    mid=ll.get_middle_node()
    print(mid.data)

    ll.reverse()
    ll.traverse()
        
