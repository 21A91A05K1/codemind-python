def palindrome(i):
    s=0
    temp=i
    while(i!=0):
        d=i%10
        s=s*10+d
        i=i//10
    if(s==temp):
        print(s,end=' ')
m=int(input())
n=int(input())
for i in range(m,n+1):
    palindrome(i)