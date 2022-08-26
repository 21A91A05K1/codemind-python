n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in a[0:(n//2):1]:
    s=s+i
for i in a[(n//2):n+1:1]:
    s1=s1+i
print(s1-s)