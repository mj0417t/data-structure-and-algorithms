class Stack:
    def __init__(self):
        self.stack=[]
    
    #O(1)
    def push(self,data):
        self.stack.append(data)

    #O(1)
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data
    
    #O(1)
    def peek(self):
        return self.stack[-1]
    
    #O(1)
    def is_empty(self):
        return self.stack==[]
    
     #O(1)
    def stack_size(self):
        return len(self.stack)
    

if __name__=='__main__':
    st=Stack()
    st.push(10)
    st.push(30)
    st.push(50)
    
    print("Size =%d" % st.stack_size())
    print("Popped Item =%d" % st.pop())
    print("Size =%d" % st.stack_size())
    print("peekes =%d" % st.peek())
    print("Size =%d" % st.stack_size())

    print('-'*25)
    while  not st.is_empty():
        print("Popped Item =%d" % st.pop())