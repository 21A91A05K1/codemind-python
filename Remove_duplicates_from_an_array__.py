n=int(input())
for i in range(0,n+1):
    a=list(map(int,input().split()))
    print(*(set(a)))
