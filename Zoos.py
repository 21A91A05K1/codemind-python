s=input()
zc=0
oc=0
for i in range(len(s)):
    if s[i] in 'z':
        zc+=1
    else:
        oc+=1
if(zc*2==oc):
    print('Yes')
else:
    print('No')