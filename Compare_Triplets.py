a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
c1=0
for i in range(0,3):
    for j in range(0,3):
        if(a[i]>b[j] and i==j):
            c+=1
        elif(b[j]>a[i] and i==j):
            c1+=1
print(c,c1)