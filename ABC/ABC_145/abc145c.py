import math
N = int(input())
X = []
Y = []
for n in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
S = 0
for i in range(N):
    for j in range(N):
        d = (X[i]-X[j])**2 + (Y[i]-Y[j])**2
        S += math.sqrt(d)
print(S/N)
