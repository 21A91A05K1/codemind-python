n=input()
n=n.split(" ")
for i in n:
    if(n.index(i)%2==0):
        i=i[::-1]
    print(i,end=' ')