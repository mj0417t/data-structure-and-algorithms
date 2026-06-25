class Sort:
    def mergeSort(self,arr,start,end):
        if start>=end:
            return
        mid=(start+end)//2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr,mid+1,end)
        self.merge(arr,start,mid,end)

    def merge(self, arr,start,mid,end):
        tmp=[]
        i=start
        j=mid+1
        while i<=mid and j<=end:
            if arr[i]<=arr[j]:
                tmp.append(arr[i])
                i+=1
            else:
                tmp.append(arr[j])
                j+=1

        while i<=mid:
            tmp.append(arr[i])
            i+=1

        while j<=end:
            tmp.append(arr[j])
            j+=1

        for i in range(start, end+1):
            arr[i]=tmp[i-start]


if __name__=='__main__':
    sort=Sort()
    arr=[4,1,2,5,3]
    sort.mergeSort(arr,0, len(arr)-1)
    print(arr)
