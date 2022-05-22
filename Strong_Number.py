def fact(d):
    i=1
    f=1
    while(i<=d):
        f=f*i
        i=i+1
    return f
n=int(input())
sum=0
temp=n
while(n):
    d=n%10
    sum=sum+fact(d)
    n=n//10
if(sum==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")