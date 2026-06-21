class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return self.queue==[]
    
    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)
    

if __name__=='__main__':
    q=Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(10)
    
    print("Size =%d" % q.size_queue())
    print("Dequeue Item =%d" % q.dequeue())

    print('-'*25)