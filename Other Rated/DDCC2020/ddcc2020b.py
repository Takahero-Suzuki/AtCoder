from collections import deque
N = int(input())
A = deque(list(map(int,input().split())))
L = 0
R = 0
while len(A) != 0:
    if L < R:
        L += A.popleft()
    else:
        R += A.pop()
print(abs(R-L))
