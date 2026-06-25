class Sort:
    def insertionSort(self,arr):
        for i in range(len(arr)):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
        return arr


if __name__=='__main__':
    sort=Sort()
    arr=[4,1,2,5,3]
    print(sort.insertionSort(arr))
