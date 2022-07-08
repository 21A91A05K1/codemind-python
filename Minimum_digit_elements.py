n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    b.append(len(str(i)))
m=min(b)
for i in a:
    if(len(str(i))==m):
        c+=1
print(c)