a=input()
b=''
for i in a:
    if i not in b:
        b+=i
if(a==b):
    print('True')
else:
    print('False')