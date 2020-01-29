S = list(input())
T = list(input())

l = len(S)
d = {chr(_): chr(_) for _ in range(97,97+26)}
for i in range(l):
    now = d[S[i]]
    change = T[i]
    for k,v in d.items():
        if now == v:
            d[k] = change
        if change == v:
            d[k] = now

ans = 'Yes'
for i in range(l):
    if d[S[i]] != T[i]:
        ans = 'No'
        break

print(ans)

'''
for i in range(len(S)):
    if d[S[i]] == 0:
        d[S[i]] = T[i]
        d[T[i]] = S[i]
    elif d[S[i]] != T[i]:
        ans = 'No'
        break
print(ans)
print(d)
'''

'''
    if S[i] not in d.keys():
        d[S[i]] = T[i]
        d[T[i]] = S[i]
    elif d[S[i]] != T[i]:
        ans = 'No'
        break
print(ans)

'''