n=int(input())
c=0
pa=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]!=-1):
        c=1
        for j in range(len(a)):
            if(a[i]==a[j] and i!=j):
                c+=1
                a[j]=-1
        pa+=c//2
print(pa)