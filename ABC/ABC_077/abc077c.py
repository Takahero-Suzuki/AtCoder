#二分探索と累積和
import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

B.sort()
C.sort()

BtoC = [0 for i in range(N)]

for i in range(N-1,-1,-1):
    x = bisect.bisect_right(C,B[i])
    if i == N-1:
        BtoC[i] = N-x
    else:
        BtoC[i] = BtoC[i+1]+N-x

#print(BtoC)

ans = 0

for a in A:
    y = bisect.bisect_right(B,a)
    if y != N:
        ans += BtoC[y]

print(ans)
