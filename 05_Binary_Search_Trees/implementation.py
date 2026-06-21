class TreeComparator:

    def compare(self, node1, node2):

        # your implementation here to compare whether two BSTs have the same topology and values or not
        # this function return with a boolean value
        if (node1 is None and node2 is None) or (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
            return node1==node2
        if node1.data != node2.data:
            return False
        return self.compare(node1.left_child, node2.left_child) and self.compare(node1.right_child, node2.right_child)
        

class Node:
    def __init__(self, data, parent=None):
        self.data=data
        self.left_child: Node| None=None
        self.right_child: Node| None=None
        self.parent=parent

class BinarySearchTree:

    def __init__(self):
        self.root=None

    def remove(self,data):
        if self.root:
            self.remove_node(data,self.root)


    def remove_node(self,data, node):
        if node is None:
            return
        
        if data<node.data:
            self.remove_node(data,node.left_child)
        elif data>node.data:
            self.remove_node(data, node.right_child)
        else:
            #leaf node case
            if node.left_child is None and node.right_child is None:
                print("Removing a leaf node...%d"% node.data)
                parent=node.parent
                if parent is not None and parent.left_child==node:
                    parent.left_child=None
                if parent is not None and parent.right_child==node:
                    parent.right_child=None

                if parent is None:
                    self.root=None
                del node
            
            #when there's a single child
            elif node.left_child is None and node.right_child is not None:
                print("Removing a node with single child...%d"% node.data)
                parent = node.parent
                if parent is not None and parent.left_child==node:
                    parent.left_child=node.right_child
                if parent is not None and parent.right_child==node:
                    parent.right_child=node.right_child
                if parent is None:
                    self.root=None
                node.right_child.parent=parent
                del node

            elif node.left_child is not None and node.right_child is None:
                print("Removing a node with single child...%d"% node.data)
                parent = node.parent
                if parent is not None and parent.left_child==node:
                    parent.left_child=node.left_child
                if parent is not None and parent.right_child==node:
                    parent.right_child=node.right_child
                if parent is None:
                    self.root=None
                node.left_child.parent=parent
                del node
            #remove node with 2 child
            else:
                print('Removing node with 2 children...')
                predecessor=self.get_predecessor(node.left_child)

                #swap the node and predecessor
                temp=predecessor.data
                predecessor.data=node.data
                node.data=temp

                self.remove_node(data,predecessor)


    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node
    

    def insert(self, data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_node(data,self.root)
    
    def insert_node(self,data,node):
        if data<node.data:
            if node.left_child:
                self.insert_node(data,node.left_child)
            else:
                node.left_child=Node(data, node)
        else:
            if node.right_child:
                self.insert_node(data,node.right_child)
            else:
                node.right_child=Node(data,node)
    
    def get_min(self):
        if self.root:
            return self.get_min_val(self.root)
    
    def get_min_val(self, node):

        if node.left_child:
            return self.get_min_val(node.left_child)

        return node.data
    
    def get_max(self):
        if self.root:
            return self.get_max_val(self.root)
    
    def get_max_val(self, node):

        if node.right_child:
            return self.get_max_val(node.right_child)
            
        return node.data
    
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        print(node.data)
        if node.right_child:
            self.traverse_in_order(node.right_child)

        

if __name__=='__main__':
    bst=BinarySearchTree()
    bst.insert(10)
    bst.insert(24)
    bst.insert(35)
    bst.insert(12)
    bst.insert(4)
    bst.insert(11)
    bst.insert(-5)
    bst.insert(-12)
    bst.insert(22)

    bst.traverse()

    print('Max Value: %s' % bst.get_max())
    print('Min Value: %s' % bst.get_min())

    # print('-'*25)
    # bst.remove(22)
    # bst.remove(10)
    # bst.remove(11)
    
    bst.traverse()

    bst2=BinarySearchTree()
    
    bst2.insert(10)
    bst2.insert(24)
    bst2.insert(35)
    bst2.insert(12)
    bst2.insert(4)
    bst2.insert(11)
    bst2.insert(-5)
    bst2.insert(-12)
    bst2.insert(22)
    t=TreeComparator()
    print(t.compare(bst.root,bst2.root))