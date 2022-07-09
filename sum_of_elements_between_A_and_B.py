n=int(input())
s=0
a=list(map(int,input().split()))
b,c=map(int,input().split())
min=a[n-1]
for i in range(len(a)):
    if(a[i]>=b and a[i]<=c):
        s=s+a[i]
print(s)