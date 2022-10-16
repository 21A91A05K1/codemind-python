t=int(input())
for i in range(t):
    a=int(input())
    c=0
    k=list(map(int,input().split()))
    for i in k:
        if(i%2!=0):
            c+=1
    print(int(c/2))