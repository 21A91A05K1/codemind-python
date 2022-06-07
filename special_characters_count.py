n=input()
c=0
for i in range(len(n)):
    if n[i] in '!@#$%^&*?_/(){}[]|;:<>,.':
        c+=1
print(c)