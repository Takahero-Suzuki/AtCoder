S = list(input())

N = len(S)
re = 0
ro = 0
le = 0
lo = 0
ans = [0 for i in range(N)]

for i in range(N):
    if S[i] == 'R':
        if S[i+1] == 'L':
            if i%2 == 0:
                ans[i] += re+1
                ans[i+1] += ro
                re = 0
                ro = 0
            else:
                ans[i] += ro+1
                ans[i+1] += re
                re = 0
                ro = 0
        else:
            if i%2 == 0:
                re += 1
            else:
                ro += 1

for i in range(N-1,-1,-1):
    if S[i] == 'L':
        if S[i-1] == 'R':
            if i%2 == 0:
                ans[i] += le+1
                ans[i-1] += lo
                le = 0
                lo = 0
            else:
                ans[i] += lo+1
                ans[i-1] += le
                le = 0
                lo = 0
        else:
            if i%2 == 0:
                le += 1
            else:
                lo += 1

print(' '.join(map(str,ans)))
