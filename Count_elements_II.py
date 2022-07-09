m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
e=set(a)
f=set(b)
for i in e:
    if i not in f:
        c+=1
for i in f:
    if i not in e:
        d+=1
print(c+d)
        