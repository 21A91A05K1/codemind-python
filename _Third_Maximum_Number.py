n=int(input())
a=list(map(int,input().split()))
b=set(a)
b=sorted(b)
if(len(b)>=3):
    print(b[-3])
else:
    print(max(b))