N,M = map(int,input().split())
friend = [[] for n in range(N)]
for m in range(M):
    A,B = map(int,input().split())
    friend[A-1].append(B)
    friend[B-1].append(A)
for i in range(N):
    ans = 0
    for j in range(N):
        if i != j and j+1 not in friend[i] and len(set(friend[i])&set(friend[j])) >= 1:
            ans += 1
    print(ans)
