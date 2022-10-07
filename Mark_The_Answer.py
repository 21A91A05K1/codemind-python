n,d=map(int,input().split())
max=0
f=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]<=d):
        max+=1
    else:
        if(f==0):
            f=1
        else:
            break
print(max)