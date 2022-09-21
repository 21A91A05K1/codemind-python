t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    m=list(map(int,input().split()))
    n=list(map(int,input().split()))
    c=[]
    for i in m:
        c.append(i)
    for i in n:
        c.append(i)
    c.sort()
    print(*c)