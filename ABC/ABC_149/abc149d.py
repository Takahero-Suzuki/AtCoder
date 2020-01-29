N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())

ans = 0
check = {i:0 for i in range(N)}
for i in range(N):
    if i <= K-1:
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        else:
            ans += S
    else:
        if T[i] != T[i-K]:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
        elif T[i] == T[i-K] and check[i-K] == 1:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R   
            else:
                ans += S
        else:
            check[i] = 1

print(ans)


