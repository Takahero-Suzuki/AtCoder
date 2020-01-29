N,K = map(int,input().split())
S = list(input())

ch = 0
ans = 0

if N != 1:
    for i in range(N):
        if i == 0:
            if S[i] != S[i+1]:
                ch += 1
            if S[i] == S[i+1] == 'R':
                ans += 1
        elif i == N-1:
            if S[i] == S[i-1] == 'L':
                ans += 1
        else:
            if S[i] != S[i+1]:
                ch += 1
            if S[i] == S[i+1] == 'R' or S[i] == S[i-1] == 'L':
                ans += 1

print(ans+min(K*2,ch))
