t=int(input())
for i in range(0,t):
    a=int(input())
    temp=a
    sum=0
    while(a):
        d=a%10
        sum=sum*10+d
        a=a//10
    if(sum==temp):
        print('True')
    else:
        print('False')