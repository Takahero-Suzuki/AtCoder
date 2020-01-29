import collections

N = int(input())
D = list(map(int,input().split()))
D_counter = collections.Counter(D)
D_max = max(D)
ans = 1
if D[0] > 0:
    ans = 0
else:
    if D_counter[0] > 1:
        ans = 0
    for n in range(1,D_max+1):
        if D_counter[n] > 0:
            for d in range(D_counter[n]):
                ans = ans * D_counter[n-1]
                ans = ans % 998244353
        else:
            ans = 0
            break
print(ans)
