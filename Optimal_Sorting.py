t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=a
    c=max(a)
    d=min(a)
    m=sorted(b)
    if(a==m):
        print(0)
    else:
        print(c-d)
        