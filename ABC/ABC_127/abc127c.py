N,M = map(int,input().split())
L0 = 1
R0 = N
for i in range(M):
    L,R = map(int,input().split())
    L0 = max(L0,L)
    R0 = min(R0,R)
print(max(R0-L0+1,0))
