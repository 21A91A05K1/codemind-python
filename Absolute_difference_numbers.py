n,size=map(int,input().split())
rev=0
rev1=0
c=0
s1=0
s2=0
temp=n
c=size
while(temp>0):
    r=temp%10;
    rev=(rev*10)+r
    temp=temp//10
while(n>0):
    r=n%10
    if(c==0):
        break
    s1=(s1*10)+r
    n=n//10
    c-=1
c=size
while(rev>0):
    r=rev%10
    if(c==0):
        break
    s2=(s2*10)+r
    rev=rev//10
    c-=1
while(s1>0):
    r=s1%10
    rev1=(rev1*10)+r
    s1=s1//10
if(rev1>s2):
    print(rev1-s2)
else:
    print(s2-rev1)