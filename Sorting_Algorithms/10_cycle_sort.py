from collections import defaultdict
class Sort:
    def cycleSort(self,arr):
        n=len(arr)
        for cycle_start in range(n-1):
            item=arr[cycle_start]
            pos=cycle_start
            for i in range(cycle_start+1,n):
                if arr[i]<item:
                    pos+=1
            if pos==cycle_start:
                continue
            while item==arr[pos]:
                pos+=1
            if pos!=cycle_start:
                arr[pos],item=item,arr[pos]
            while pos!=cycle_start:
                pos=cycle_start
                for i in range(cycle_start+1,n):
                    if arr[i]<item:
                        pos+=1
                while item==arr[pos]:
                    pos+=1
                if item!=arr[pos]:
                    arr[pos],item=item,arr[pos]


if __name__=='__main__':
    sort=Sort()
    arr=[5,2,3,1,4]
    n=len(arr)
    if n==1:
        print(arr)
    sort.cycleSort(arr)
    print(arr)