n=input()
n=n.split()
m=99
for i in n:
    l=len(i)
    if(m>l):
        m=l
print(m)
