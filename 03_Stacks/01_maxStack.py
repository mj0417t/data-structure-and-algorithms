class Stack:
    def __init__(self):
        self.stack=[]
        self.maxStack=[]
    
    #O(1)
    def push(self,data):
        self.stack.append(data)
        if(len(self.stack)==1):
            self.maxStack.append(data)
            return
        if data > self.maxStack[-1]:
            self.maxStack.append(data)
        else:
            self.maxStack.append(self.maxStack[-1])
        
    

    #O(1)
    def pop(self):
        data=self.stack[-1]
        while self.maxStack!=[] and data==self.maxStack[-1]:
            del self.maxStack[-1]
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
    
    def getMax(self):
        return self.maxStack[-1]
    

if __name__=='__main__':
    st=Stack()
    st.push(10)
    st.push(30)
    st.push(50)
    st.push(10)
    st.push(20)
    st.push(10)
    
    print("Size =%d" % st.stack_size())
    print("Max item", st.getMax())
    print("Popped Item =%d" % st.pop())
    print("Size =%d" % st.stack_size())
    print("peekes =%d" % st.peek())
    print("Size =%d" % st.stack_size())
    print("Max item", st.getMax())
    

    print('-'*25)
    while  not st.is_empty():
        print("Popped Item =%d" % st.pop())