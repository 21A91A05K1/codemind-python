n=int(input())
a=list(map(int,input().split()))
b=min(a)
f=0
for i in range(b,0,-1):
    f=0
    for j in range(len(a)):
        if(a[j]%i!=0):
            f=1
            break
    if(f==0):
        print(i)
        break