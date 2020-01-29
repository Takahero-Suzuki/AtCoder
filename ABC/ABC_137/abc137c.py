import collections
N = int(input())
S = [list(input()) for i in range(N)]

for i in range(N):
    Si = S[i]
    Si.sort()
    Si2 = ''.join(Si)
    S[i] = Si2

ans = 0
Sc = collections.Counter(S).most_common()
for s in Sc:
    ans += s[1]*(s[1]-1)//2

print(ans)
'''
# O(N^2)はTLE!!
import collections
N = int(input())
S = [list(input()) for i in range(N)]
ans = 0
for i in range(N-1):
    Si = collections.Counter(S[i]).most_common()
    Si.sort(key=lambda x: x[0])
    for j in range(i+1,N):
        Sj = collections.Counter(S[j]).most_common()
        Sj.sort(key=lambda x: x[0])
        if Si == Sj:
            ans += 1
print(ans)
'''



        



