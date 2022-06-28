def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            break
    else:
        if(n!=1):
            return n
n=int(input())
c=0
a=list(map(int,input().split()))
k=int(input())
for i in range(len(a)):
    if(a[i]<=k and prime(a[i])):
        c+=1
print(c)