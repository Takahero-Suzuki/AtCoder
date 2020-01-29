N = int(input())
A = sorted(list(map(int,input().split())))
P = 10**9+7
if N%2 == 0:
    check = [i if i%2 == 1 else i+1 for i in range(N)]
else:
    check = [i if i%2 == 0 else i+1 for i in range(N)]
if A == check:
    ans = 1
    for i in range(N//2):
        ans *= 2
        ans %= P
else:
    ans = 0
print(ans)
