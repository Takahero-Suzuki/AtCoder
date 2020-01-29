S = list(input())
small = [chr(i) for i in range(97,97+26)]
count = 0
ans = 'AC'
for i in range(len(S)):
    if i == 0:
        if S[i] != 'A':
            ans = 'WA'
            break
    elif i == 1:
        if S[i] not in small:
            ans = 'WA'
            break
    elif i != len(S)-1:
        if S[i] == 'C':
            count += 1
        elif S[i] not in small:
            ans = 'WA'
            break
    else:
        if S[i] not in small:
            ans = 'WA'
if ans == 'AC' and count != 1:
    ans = 'WA'
print(ans)
