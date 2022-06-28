n=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(len(a)):
    sum=0
    while(a[i]):
        d=a[i]%10
        sum=sum*10+d
        a[i]=a[i]//10
    print(sum,end=' ')