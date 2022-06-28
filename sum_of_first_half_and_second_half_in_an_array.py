n=int(input())
s1=0
s2=0
a=list(map(int,input().split()))
for i in range(0,(n//2)+1):
    s1=s1+i
for j in range((n//2)+1,n+1):
    s2=s2+j
print(s1)
print(s2)