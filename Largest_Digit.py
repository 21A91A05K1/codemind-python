n=int(input())
lar=0
while(n>0):
    d=n%10
    n=n//10
    if(d>lar):
        lar=d
print(lar)