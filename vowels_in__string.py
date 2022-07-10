n=input()
c=0
a=' '
for i in n:
    if i not in a:
        a+=i
for i in a:
    if i in 'aeiouAEIOU':
        c+=1
        print(i,end=' ')
if(c==0):
    print('-1')