from collections import defaultdict
class Sort:
    def cycleSort(self,arr):
        n=len(arr)
        i=0
        while i<n:
            correct=arr[i]-1
            if arr[i]!=arr[correct]:
                arr[i],arr[correct]=arr[correct],arr[i]
            else:
                i+=1


if __name__=='__main__':
    sort=Sort()
    arr=[5,2,3,1,4]
    n=len(arr)
    if n==1:
        print(arr)
    sort.cycleSort(arr)
    print(arr)