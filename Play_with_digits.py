n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(len(a)):
    while(a[i]):
        d=a[i]%10
        s=s+d
        a[i]=a[i]//10
print(s)