n=input()
n=n.split()
m=0
for i in n:
    a=len(i)
    if(m<a):
        m=a
print(m)