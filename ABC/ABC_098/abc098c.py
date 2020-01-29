import collections
N = int(input())
S = list(input())
rightE = S.count('E')
rightW = S.count('W')
leftE = 0
leftW = 0
ans = N
for n in range(N):
    if S[n] == 'E':
        rightE -= 1
        ans = min(ans,leftW+rightE)
        leftE += 1
    else:
        rightW -= 1
        ans = min(ans,leftW+rightE)
        leftW += 1
print(ans)
