def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
c=0
for i in range(2,n+1):
    for j in range(2,n+1):
        if(prime(i) and prime(j) and i*j==n and i<j):
            print(i,j)
            c+=1
if(c==0):
    print('-1')
    