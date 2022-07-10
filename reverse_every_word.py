n=input()
n=n.split()
a=[]
for i in n:
    a.append(i[::-1])
print(' '.join(a))