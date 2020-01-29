S = list(input().split('><'))
if len(S) != 1:
    for n in range(len(S)):
        if n == 0:
            S[n] = S[n] + '>'
        elif n == len(S)-1:
            S[n] = '<' + S[n]
        else:
            S[n] = '<' + S[n] + '>'
ans = 0
for n in range(len(S)):
    a = S[n].count('<')
    b = len(S[n])-a
    if a >= b:
        ans += a*(a+1)//2
        ans += b*(b-1)//2
    else:
        ans += b*(b+1)//2
        ans += a*(a-1)//2
print(ans)
