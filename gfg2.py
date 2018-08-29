#code
#Question url:https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0/?ref=self
def findsum(arr,s,x):
    s=s+arr[0]
    if(s<x):
        return findsum(arr[1:],s,x)
    elif(s==x):
        return 0;
    else:
        return -1
n=int(input())
for i in range(n):
    k=[]
    t=list(map(int,input().split()))
    l=list(map(int,input().split()))
    for j in range(t[0]):
        f=0
        o=findsum(l[j:],0,t[1])
        if(o==0):
            sum1=0
            count=0
            for i in l[j:]:
                
                count=count+1
                sum1=i+sum1
                if(sum1==t[1]):
                    k.append(j+1)
                    k.append(j+count)
                    f=1
                    break
        if(f==1):
            break
    print(k[0], end=" ")
    print(k[1])
                
