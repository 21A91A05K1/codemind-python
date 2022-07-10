n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(i<0):
        i=-i
    b.append(len(str(i)))
print(*b)