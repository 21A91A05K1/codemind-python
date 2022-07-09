n=int(input())
s=0
a=list(map(int,input().split()))
b,c=map(int,input().split())
max=a[0]
for i in range(len(a)):
    if(a[i]>=b and a[i]<=c):
        if(max<a[i]):
            s+=1
            max=a[i]
if(s==0):
    print("-1")
else:
    print(max)