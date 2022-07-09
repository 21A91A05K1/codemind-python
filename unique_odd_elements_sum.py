n=int(input())
s=0
a=list(map(int,input().split()))
a=set(a)
for i in a:
    if i%2!=0:
        s=s+i
print(s)
