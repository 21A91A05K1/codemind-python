n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]==0 or a[i]==1):
        c+=1
if(c==n):
    print('True')
else:
    print('False')