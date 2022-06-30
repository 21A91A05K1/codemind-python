def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
m=int(input())
n=int(input())
t=m+n
i=1
while(1):
    q=t+i
    if(prime(q)):
        print(i)
        break
    i+=1