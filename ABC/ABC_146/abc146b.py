N = int(input())
S = list(input())
for n in range(len(S)):
    S[n] = ord(S[n])
    S[n] += N
    if S[n] > 90:
        S[n] -= 26
    S[n] = chr(S[n])
print(''.join(S))
