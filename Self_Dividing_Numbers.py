def dividing(n):
    c=0
    temp=n
    l=len(str(n))
    while(n!=0):
        d=n%10
        if(d!=0):
            if(temp%d==0):
                c+=1
        n=n//10
    if(c==l):
        return temp
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(dividing(i)):
        print(i,end=' ')