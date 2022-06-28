def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            break
    else:
        if(n!=1):
            return n
n=int(input())
sum=0
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(prime(a[i])):
        sum=sum+a[i]
        c+=1
ave=sum/c
print('%.2f'%ave)
    