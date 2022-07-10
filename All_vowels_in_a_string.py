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
    if i in b:
        c+=1
if(c==5):
    print('True')
else:
    print('False')