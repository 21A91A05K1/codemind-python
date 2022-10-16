m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(m):
    c1=0
    for j in range(i,m):
        c1+=a[j]
        if(c1==n):
            c+=1
print(c)