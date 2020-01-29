N = int(input())
A = list(map(int,input().split()))

mc = 0
absum = 0
absmin = 10**9+7

for a in A:
    if a < 0:
        mc += 1
    absum += abs(a)
    absmin = min(absmin,abs(a))

if mc%2 == 0:
    ans = absum
else:
    ans = absum-absmin*2

print(ans)
