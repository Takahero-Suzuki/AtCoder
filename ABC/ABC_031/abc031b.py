L,H = map(int,input().split())
N = int(input())
for n in range(N):
    A = int(input())
    if A > H:
        print(-1)
    elif L <= A:
        print(0)
    else:
        print(L-A)
