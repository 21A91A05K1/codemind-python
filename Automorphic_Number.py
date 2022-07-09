n=int(input())
c=1
temp=n
s=n*n
while(n!=0):
    c=c*10
    n=n//10
if(s%c==temp):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')