class Sort:
    def selectionSort(self,arr):
        for i in range(len(arr)-1):
            mini=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[mini]:
                    mini=j
            arr[mini],arr[i]=arr[i],arr[mini]
        return arr


if __name__=='__main__':
    sort=Sort()
    arr=[4,1,2,5,3]
    print(sort.selectionSort(arr))
