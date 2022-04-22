import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
s1=math.sqrt(area)
print('%.2f'%s1)