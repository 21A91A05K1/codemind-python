n=input()
c=0
a=' '
b=' '
m='aeiou'
for i in n:
    if i not in a:
        a+=i
for i in a:
    if i in m:
        b+=i
for i in m:
    if i not in b:
        c+=1
        print(i,end=' ')
if(c==0):
    print('0')