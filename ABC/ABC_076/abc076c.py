S = list(input())
T = list(input())
lenS = len(S)
lenT = len(T)
change = 0
for i in range(lenS-lenT,-1,-1):
    a = 1
    for j in range(lenT):
        if S[i+j] != T[j] and S[i+j] != '?':
            a = 0
    if a == 1:
        for j in range(lenT):
            S[i+j] = T[j]
        change = 1
        break

for i in range(lenS):
    if S[i] == '?':
        S[i] = 'a'

if change == 1:
    print(''.join(S))
else:
    print('UNRESTORABLE')
