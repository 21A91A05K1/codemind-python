n=input()
c=0
for i in range(len(n)):
    if n[i] in ' ':
        c+=1
print(c+1)