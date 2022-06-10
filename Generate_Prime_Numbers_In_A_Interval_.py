m=int(input())
n=int(input())
for a in range(m,n+1):
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            break
    else:
        if(a!=1):
            print(a)