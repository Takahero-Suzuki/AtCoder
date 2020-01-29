import itertools
N,M = map(int,input().split())
switch = [list(map(int,input().split())) for m in range(M)]
p = list(map(int,input().split()))
# スイッチのONとOFFの組合せ(1がONで0がOFF)
S = list(itertools.product([0,1], repeat=N))
ans = 0
for s in S:
    s_ok = 0
    # 全ての電球に対して
    for m in range(M):
        count = 0
        # 1つの電球の全てのスイッチに対して
        for i in range(1, switch[m][0]+1):
            if s[switch[m][i]-1] == 1:
                count += 1
        if count%2 == p[m]:
            s_ok += 1
        else:
            break
    if s_ok == M:
        ans += 1
print(ans)
