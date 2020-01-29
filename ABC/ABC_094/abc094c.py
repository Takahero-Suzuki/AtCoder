N=int(input())
X=list(map(int,input().split()))

X_sort=sorted(X)

if X_sort[N//2-1]==X_sort[N//2]:
    for n in range(N):
        print(X_sort[N//2])
else:
    if X_sort.count(X_sort[N//2-1])==1:
        for n in range(N):
            if X[n]>X_sort[N//2-1]:
                print(X_sort[N//2-1])
            else:
                print(X_sort[N//2])
    else:
        for n in range(N):
            if X[n]>X_sort[N//2-1]:
                print(X_sort[N//2-1])
            else:
                print(X_sort[N//2])
