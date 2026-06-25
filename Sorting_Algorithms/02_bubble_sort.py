class Sort:
    def bubbleSort(self,arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr


if __name__=='__main__':
    sort=Sort()
    arr=[4,1,2,5,3]
    print(sort.bubbleSort(arr))
