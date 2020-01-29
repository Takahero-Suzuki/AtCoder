A,B,C = map(int,input().split())
K = int(input())
S = A+B+C-max(A,B,C)
M = max(A,B,C)
for k in range(K):
    M = M*2
print(M+S)
