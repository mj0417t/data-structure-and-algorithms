class Sort:
    def heapSort(self,arr):
        #build heap
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
        
        #extract max and minimize heap size
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,i,0)

    def heapify(self,arr,n,i):

        l_node=(i<<1)+1
        r_node=(i<<1)+2
        largest_node=i

        if l_node<n and arr[l_node]>arr[largest_node]:
            largest_node=l_node

        if r_node<n and arr[r_node]>arr[largest_node]:
            largest_node=r_node
        
        if largest_node!=i:
            arr[i],arr[largest_node]=arr[largest_node],arr[i]
            self.heapify(arr,n,largest_node)

if __name__=='__main__':
    sort=Sort()
    arr=[4,1,2,5,3]
    sort.heapSort(arr)
    print(arr)
