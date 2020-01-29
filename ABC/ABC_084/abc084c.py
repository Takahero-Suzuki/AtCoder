import math
N = int(input())
C = []
S = []
F = []
for _ in range(N-1):
    c,s,f = map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)
for i in range(N):
    time = 0
    for j in range(i,N-1):
        if time <= S[j]:
            time = S[j]+C[j]
        else:
            time = S[j]+C[j]+F[j]*math.ceil((time-S[j])/F[j])
    print(time)
