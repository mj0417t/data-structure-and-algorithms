from collections import defaultdict
class Sort:
    def shellSort(self,arr,n):
        gap=n//2
        while gap>=1:
            for i in range(gap,n):
                tmp=arr[i]
                j=i-gap
                while j>=0 and arr[j]>tmp:
                    arr[j+gap]=arr[j]
                    j-=gap
                arr[j+gap]=tmp
            gap//=2
                
    






if __name__=='__main__':
    sort=Sort()
    arr=[5,2,3,1]
    n=len(arr)
    if n==1:
        print(arr)
    sort.shellSort(arr,n)
    print(arr)