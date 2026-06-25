class Sort:
    # def quickSort(self,arr,start,end):
    #     if start<end:
    #         pivot=self.find_pivot(arr,start,end)
    #         self.quickSort(arr, start, pivot-1)
    #         self.quickSort(arr,pivot+1,end)

    # def find_pivot(self, arr,start,end):
    #     pivot=start
    #     i=start
    #     j=end
    #     while i <j:
    #         while arr[i]<=arr[pivot] and i<=end-1:
    #             i+=1
    #         while arr[j]>arr[pivot] and j>=start+1:
    #             j-=1
    #         if i<j:
    #             arr[i],arr[j]=arr[j],arr[i]
    #     arr[start],arr[j] = arr[j],arr[start] 
    #     return j

    def quickSort(self,arr,left,right):
        if right<=left+1:
            if right==left+1 and arr[right]<arr[left]:
                arr[left],arr[right]=arr[right],arr[left]
            return
        pivot=self.partition(arr,left,right)
        self.quickSort(arr, left, pivot-1)
        self.quickSort(arr,pivot+1,right)
    
    def partition(self,arr,left,right):
        mid= (left+right)>>1
        arr[mid],arr[left+1]=arr[left+1],arr[mid]
        if arr[left]>arr[right]:
            arr[left],arr[right]=arr[right],arr[left]
        if arr[left+1]>arr[right]:
            arr[left+1],arr[right]=arr[right],arr[left+1]
        if arr[left]>arr[left+1]:
            arr[left],arr[left+1]=arr[left+1],arr[left]
        pivot=arr[left+1]
        i=left+1
        j=right

        while True:
            while True:
                i+=1
                if not arr[i]<pivot:
                    break
            while True:
                j-=1
                if not arr[j]>pivot:
                    break
            if i>j:
                break
            arr[i],arr[j]=arr[j],arr[i]
        arr[left+1],arr[j]=arr[j],arr[left+1]
        return j





if __name__=='__main__':
    sort=Sort()
    arr=[5,2,3,1]
    sort.quickSort(arr,0, len(arr)-1)
    print(arr)
