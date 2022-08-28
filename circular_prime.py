def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            break
    else:
        return 1
n=int(input())
s=0
if(prime(n)):
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(prime(s)):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')