n=int(input())
sum=0
while(sum==0 or sum>9):
    sum=0
    while(n>0):
        d=n%10
        sum=sum+d
        n=n//10
    n=sum;
print(n)