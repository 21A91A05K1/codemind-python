a=input()
b=a.split()
c='aeiou'
d=0
for i in b:
    d=0
    for j in i:
        if j in c:
            d+=1
    print(d,end=' ')