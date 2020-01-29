N,K = map(int,input().split())
a = list(map(int,input().split()))

i = 0
j = 0
s = 0

ans = 0

while i < N:

    while s < K and i < N:
        s += a[i]
        i += 1
        ans += j

    while s >= K:
        s -= a[j]
        j += 1
        ans += 1

print(ans)
