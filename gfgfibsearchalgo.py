import time
def fib(x,arr):
    '''
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
    '''
    f1=0
    f2=1
    f3=f2+f1
    # f1,f2,f3 are the 3 fibonacci terms
    while(f3>len(arr)):
        f1=f2
        f2=f3
        f3=f1+f2
    offset=-1
    while(f3>1):
        i=min(offset+f1,len(arr)-1)
        if(arr[i]<x):
            f3=f2
            f2=f1
            f1=f3-f2
            offset=i
        elif(arr[i]>x):
            f3=f1
            f2=f2-f1
            f3=f1-f2
        else:
            return i
    if(f2 and arr[offset+1]):
        return offset+1;
    return -1
arr=[1,2,2,3,453,4353,43200]
x=4353
start=time.time()
loc=fib(x,arr)
end=time.time()
print(loc)
print(end-start)

    
