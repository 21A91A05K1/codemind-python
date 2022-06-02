import math
t=int(input())
for i in range(t):
    n=int(input())
    s=int(math.sqrt(n))
    if(int(s*s)==n):
        print('True')
    else:
        print('False')