s=input()
a='!@#$%^&*()_+-=|?/.,><~`'
c=0 
e=[]
o=[]
for i in s:
    if i in a:
        c+=1
    if(i.isdigit()):
        if(int(i)%2==0):
            e.append(i)
        else:
            o.append(i)
i,j=0,0
if(c%2==0):
    while(i<len(e) or j<len(o)):
        if(i<len(e)):
            print(e[i],end="")
        if(j<len(o)):
            print(o[i],end='')
        i+=1
        j+=1
else:
    while(i<len(e) or j<len(o)):
        if(i<len(o)):
            print(o[i],end="")
        if(j<len(e)):
            print(e[i],end='')
        i+=1
        j+=1
