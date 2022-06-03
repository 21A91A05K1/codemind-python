n=input()
s=0
for i in range(len(n)):
    if n[i] in '0123456789':
        s=s+int(n[i])
print(s)