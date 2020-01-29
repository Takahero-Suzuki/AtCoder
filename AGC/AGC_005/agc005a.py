X = input()
N = len(X)
S = 0
ans = 0
for i in range(N):
    if X[i] == 'S':
        S += 1
    elif S > 0:
        S -= 1
        ans += 2
print(N-ans)
