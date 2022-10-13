s=input()
f=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if(i!=j):
            if(s[i]==s[j]):
                c=c+1
    if(c==0):
        f=1
        print(i)
        break
if(f==0):
    print("-1")