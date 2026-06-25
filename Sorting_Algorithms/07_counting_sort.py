from collections import defaultdict
class Sort:
    def countingSort(self,arr):
        cnt=defaultdict(int)
        minVal, maxVal=min(arr),max(arr)
        for val in arr:
            cnt[val]+=1
        idx=0
        for val in range(minVal,maxVal+1):
            while cnt[val]>0:
                arr[idx]=val
                idx+=1
                cnt[val]-=1






if __name__=='__main__':
    sort=Sort()
    arr=[5,2,3,1]
    sort.countingSort(arr)
    print(arr)
