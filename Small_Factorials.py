def fact(a):
    while(a!=0):
        if(a==1):
            return a
        return a*fact(a-1)
        
t=int(input())
for i in range(t):
    a=int(input())
    print(fact(a))  