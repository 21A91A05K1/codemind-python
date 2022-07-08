n=int(input())
m=[]
a=list(map(int,input().split()))
for i in a:
    if i not in m:
        m.append(i)
print(*m)