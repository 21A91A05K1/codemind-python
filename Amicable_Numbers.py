m=int(input())
n=int(input())
sum=0
sum1=0
for i in range(1,(m//2)+1):
    if(m%i==0):
        sum=sum+i
for i in range(1,(n//2)+1):
    if(n%i==0):
        sum1=sum1+i
if(m==sum1 and n==sum):
    print('Amicable')
else:
    print('Not Amicable')