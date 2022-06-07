n=input()
c=0
for i in range(len(n)):
    if n[i] not in ' ':
        c+=1
print(c)