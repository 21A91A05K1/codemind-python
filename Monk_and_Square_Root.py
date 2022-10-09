t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    n=-1
    for i in range(b):
        if((i*i)%b==a):
            n=i
            break
    print(n)