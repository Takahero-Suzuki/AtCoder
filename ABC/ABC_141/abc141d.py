#二分探索を使った解法
import bisect
N,M = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
while M != 0:
    x = bisect.bisect_left(A,A[-1]//2)
    if N-x <= M:
        M -= N-x
        for i in range(x,N):
            A[i] = A[i]//2
        A.sort()
    else:
        for i in range(N-M,N):
            A[i] = A[i]//2
        M = 0
        A.sort()

print(sum(A))

#Priority Queueを使った解法
import heapq

N,M = map(int,input().split())
A = list(map(lambda x:(-1)*int(x),input().split()))

heapq.heapify(A)

for i in range(M):
    a = heapq.heappop(A)
    heapq.heappush(A,(-1)*(-a//2))

print(-sum(A))