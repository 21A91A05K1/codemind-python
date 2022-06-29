n=input()
c=0
for i in range(len(n)):
    if n[i] in 'abcdefghijklmnopqrstuvwxyz':
        c+=1
print(c)
        