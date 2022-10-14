n=int(input())
for i in range(n):
    c=0
    s=input().split()
    s1=input()
    k=[]
    m=[]
    for i in s1.split():
        k.append(int(i))
    for j in range(len(k)):
        su=0
        for l in range(j,len(k)):
            su=su+k[l]
            if(su==int(s[1])):
                c=1
                print(j+1,l+1)
        if(c==1):
            break
    if(c==0):
        print("-1")