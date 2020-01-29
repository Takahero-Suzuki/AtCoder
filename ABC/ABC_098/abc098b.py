import collections
N = int(input())
Y = list(input())
X = []
ans = 0
for n in range(N):
    X.append(Y.pop(0))
    X_and_Y = set(X) & set(Y)
    ans = max(ans,len(X_and_Y))
print(ans)
