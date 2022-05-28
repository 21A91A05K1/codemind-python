n=input()
vc=0
cc=0
dc=0
sc=0
for i in range(len(n)):
    if n[i] in 'aeiou':
        vc+=1
    if n[i] not in 'aeiou1234567890 ':
        cc+=1
    if n[i] in '1234567890':
        dc+=1
    if n[i] in ' ':
        sc+=1
print('Vowels:',vc)
print('Consonants:',cc)
print('Digits:',dc)
print('White spaces:',sc)