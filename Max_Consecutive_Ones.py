n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    c=0
    for j in range(i,n):
        if(a[j]==1):
            c+=1
        else:
            break
    b.append(c)
print(max(b))