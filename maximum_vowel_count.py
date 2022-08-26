a=input()
b=a.split()
d='aeiou'
e=[]
for i in b:
    c=0
    for j in i:
        if j in d:
            c+=1
    e.append(c)
print(max(e))