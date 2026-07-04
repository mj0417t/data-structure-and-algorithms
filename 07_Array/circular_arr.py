#circular arr  using extra space
def prints(a,n,idx):
    # b=[None]*2*n
    # i=0

    # #copying items in a in b twice
    # while i<n:
    #     b[i]=b[n+i]=a[i]
    #     i+=1
    
    # i=idx
    # while i<n+idx:
    #     print(b[i],end=" ")
    #     i+=1

    i=idx
    while i< idx+n:
        print(a[i%n],end=' ')
        i+=1

a=['A','B','C','D','E']
n=len(a)
prints(a,n,3)