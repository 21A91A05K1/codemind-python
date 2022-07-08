n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
m=[]
for i in range(len(a)):
    if a.count(a[i])==k:
        if a[i] not in m:
            m.append(a[i])
        c+=1
if(c==0):
    print('-1')
else:
    print(*m)