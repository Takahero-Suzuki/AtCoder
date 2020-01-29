H = int(input())
W = int(input())
N = int(input())
ans = 0
p = 0
while p < N:
    p += max(H,W)
    ans += 1

print(ans)

