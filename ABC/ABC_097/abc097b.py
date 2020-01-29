import math
X = int(input())
N = int(math.sqrt(X))+1
ans = 1
for n in range(2,N):
    b = n
    while b*n <= X:
        b = b*n
    if ans < b:
        ans = b
print(ans)
