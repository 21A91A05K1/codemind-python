n=int(input())
a=list(map(str,input().split()))
b=[]
for i in a:
    b.append(len(i))
m=max(b)
for i in a:
    if(len(i)==m):
        print(i,end=' ')