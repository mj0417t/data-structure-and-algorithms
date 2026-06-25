from collections import defaultdict
class Sort:
    def countingSort(self,arr,n,d):
        cnt=[0]*10
        for val in arr:
            cnt[(val//d)%10]+=1

        for i in range(1,10):
            cnt[i]+=cnt[i-1]

        res=[0]*n

        for i in range(n-1,-1,-1):
            idx=(arr[i]//d)%10
            res[cnt[idx]-1]=arr[i]
            cnt[idx]-=1

        for i in range(n):
            arr[i]=res[i]


    def radixSort(self,arr):
        n=len(arr)
        maxVal=max(arr)
        d=1
        while maxVal//d >0:
            self.countingSort(arr,n,d)
            d=d*10
    






if __name__=='__main__':
    sort=Sort()
    arr=[5,2,3,1]

    negatives=[-num for num in arr if num<0]
    positives=[num for num in arr if num>=0]

    if negatives:
        sort.radixSort(negatives)
        negatives=[-num for num in reversed(negatives)]

    if positives:
        sort.radixSort(positives)

    arr= negatives+positives
    print(arr)
