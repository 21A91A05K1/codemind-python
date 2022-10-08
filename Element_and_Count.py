n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in range(len(b)):
    print(b[i],a.count(b[i]),end=' ')