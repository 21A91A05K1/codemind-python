n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    if(a[i]%2!=0):
        s=s+a[i]
    if(a[i]%2==0):
        break
print(s)