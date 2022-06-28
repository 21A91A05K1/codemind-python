m,n=map(int,input().split())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]%n!=0):
        c+=1
print(c)