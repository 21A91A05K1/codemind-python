n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    temp=i
    s=0
    while(i):
        d=i%10
        s=s*10+d
        i=i//10
    if(temp==s):
        c+=1
print(c)