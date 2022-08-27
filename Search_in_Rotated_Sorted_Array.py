m=int(input())
n=list(map(int,input().split()))
a=int(input())
c=0
for i in range(len(n)):
    if(n[i]==a):
        b=i
        c+=1
if(c==0):
     print('-1')
else:
    print(b)