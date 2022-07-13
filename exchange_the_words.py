n=input()
n=n.split()
for i in range(len(n)):
    print(*n[::-1])
    break