n=int(input())
c=0
for i in range(n):
    a=input()
    c=0
    for j in range(len(a)):
        if a[j] in '0123456789':
            c+=1
    if(c!=0):
        print('Yes')
    else:
        print('No')