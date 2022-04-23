n=int(input())
sum=0
s=n*n
while(s>0):
    d=s%10
    sum=sum+d
    s=s//10
if(n==sum):
    print('Neon Number')
else:
    print('Not Neon Number')