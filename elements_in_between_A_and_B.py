n=int(input())
s=0
a=list(map(int,input().split()))
b,c=map(int,input().split())
for i in range(len(a)):
    if(a[i]>=b and a[i]<=c):
        print(a[i],end=' ')
        s+=1
if(s==0):
    print("-1")