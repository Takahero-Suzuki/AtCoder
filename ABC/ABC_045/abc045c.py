#bit全探索
import itertools

S = input()
N = len(S)
#print(S)

ans = 0
for v in itertools.product([1,0],repeat=N-1):
    start = 0
    for i in range(N-1):
        if v[i] == 1:
            stop = i+1
            ans += int(S[start:stop])
            start = stop
    ans += int(S[start:N])

print(ans)
