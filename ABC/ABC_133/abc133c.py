import itertools
L,R = map(int,input().split())
if R-L >= 2018:
    ans = 0
else:
    ij = [i%2019 for i in range(L, min(L+2019, R+1))]
    ans = 2018
    for v in itertools.combinations(ij, 2):
        ans = min(ans, (v[0]*v[1])%2019)
print(ans)
