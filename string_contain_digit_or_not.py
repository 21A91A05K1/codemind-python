n=input()
c=0
for i in range(len(n)):
    if n[i] in '0123456789':
        c+=1
if(c==0):
    print("Doesn't contain digit")
else:
    print('Contains',c,'digit')