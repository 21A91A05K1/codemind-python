m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
e=set(a)
f=set(b)
for i in e:
    if i in f:
        c+=1
print(c)