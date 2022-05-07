n=int(input())
c=0
dc=0
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        print('Not Mega Prime')
        break
else:
    while(n):
        d=n%10
        n=n//10
        c+=1
        if(d==2 or d==3 or d==5 or d==7):
            dc+=1
    if(c==dc):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
