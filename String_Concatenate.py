a=input()
b=input()
d=[]
for i in a:
    d.append(i)
for i in b:
    d.append(i)
d.sort()
print(*d,sep='')