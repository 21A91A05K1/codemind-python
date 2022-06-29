n=int(input())
a=[]
while(n):
    d=n%10
    a.append(d)
    n=n//10
for i in range(len(a)):
    if(a.count(a[i])>=2):
        print('Not Unique Number')
        break
else:
    print('Unique Number')