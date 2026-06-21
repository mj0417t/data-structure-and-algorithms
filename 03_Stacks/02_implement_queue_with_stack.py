class Queue:
    def __init__(self):
        self.enqueue_stack=[]
        self.dequeue_stack=[]

    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0:
            raise Exception("stacks are empty")
        
        if len(self.dequeue_stack)==0:
            while len(self.enqueue_stack)!=0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()
    
    

if __name__=='__main__':
    q=Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(10)
    print("Dequeue Item =%d" % q.dequeue())

    print('-'*25)