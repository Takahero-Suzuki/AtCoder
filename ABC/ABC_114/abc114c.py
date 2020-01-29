import itertools

N = int(input())

l = len(str(N))

ans = 0
for i in range(1,l+1):
    for v in itertools.product(['3','5','7'],repeat=i):
        if '3' in v and '5' in v and '7' in v:
            n = int(''.join(list(v)))
            if n <= N:
                ans += 1

print(ans)

