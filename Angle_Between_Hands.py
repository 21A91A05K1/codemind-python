h,m=map(int,input().split(':'))
a=abs(h*30-(11*m)/2)
b=360-a
if(a<b):
    if(a>abs(a)):
        print("%.1f"%a)
    else:
        print(abs(a))
else:
    if((b)>abs(b)):
        print("%.1f"%b)
    else:
        print(abs(b))