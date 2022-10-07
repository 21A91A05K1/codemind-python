m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i in b:
        c.append(i)
d=[]
for i in c:
    if i not in d:
        d.append(i)
print(*d)