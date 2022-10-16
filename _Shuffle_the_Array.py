n=int(input())
a=list(map(int,input().split()))
c=n//2
b=[]
for i in range(c):
    b.append(a[i])
    b.append(a[i+c])
print(*b)