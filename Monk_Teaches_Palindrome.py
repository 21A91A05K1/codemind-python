t=int(input())
for i in range(t):
    n=input()
    m=n
    a=m[::-1]
    if(n==a and len(a)%2==0):
        print("YES EVEN")
    elif(n==a and len(a)%2!=0):
        print("YES ODD")
    else:
        print("NO")