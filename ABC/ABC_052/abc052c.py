N = int(input())
if N == 1:
    print(1)
    exit()
P = 10**9+7
d = {}
for i in range(2,N+1):
    k = i
    for j in range(2,i):
        while i%j == 0:
            i = i//j
            if j in d.keys():
                d[j] += 1
            else:
                d[j] = 1
    if k == i:
        d[i] = 1
ans = 1
for v in d.values():
    ans = ans*(v+1)%P
print(ans)
