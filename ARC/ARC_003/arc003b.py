N = int(input())
S = [input()[::-1] for _ in range(N)]
S.sort()

for i in range(N):
    print(S[i][::-1])
