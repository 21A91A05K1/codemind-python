import math
n=int(input())
s=0
temp=n
c=len(str(n))
while(n):
    d=n%10
    s=s+pow(d,c)
    n=n//10
    c=c-1
if(s==temp):
    print('True')
else:
    print('False')
