N,A,B = map(int,input().split())
S = [int(input()) for i in range(N)]
M = max(S)
m = min(S)
if M == m:
    print(-1)
else:
    P = B/(M-m)
    Q = A-sum(S)/N*P
    print(P,Q)
