n=int(input())
s=0
a=list(map(int,input().split()))
b,c=map(int,input().split())
min=a[n-1]
for i in range(len(a)):
    if(a[i]>=b and a[i]<=c):
        if(min>a[i]):
            s+=1
            min=a[i]
if(s==0):
    print("-1")
else:
    print(min)