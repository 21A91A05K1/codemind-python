n=int(input())
a=list(map(int,input().split()))
m=[]
c=0
for i in a:
    if i==a.count(i):
        c+=1
        m.append(i)
if(c==0):
    print('-1')
else:
    print(min(m),max(m),end=' ')