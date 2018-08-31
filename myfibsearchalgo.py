import time
def fib(arr,x):
    f1=0
    f2=1
    f3=f1+f2
    while(f3<len(arr)):
        f1=f2
        f2=f3
        f3=f1+f2
        t=bins(arr,f1,f3,x);
        if(t!=-1):
            return t;
    return -1
def bins(arr,l,h,x):
    while(l<=h):
        m=int((l+h)/2)
        if(arr[m]<x):
            l=m+1
        elif(arr[m]>x):
            h=m-1
        else:
            return m
    return -1
arr=[]
for i in range(1,1000,2):
    arr.append(i)
x=799
start=time.time()
loc=fib(arr,x)
end=time.time()
print(loc)
print(end-start)

    
