N = int(input())
H = list(map(int,input().split()))
H.append(0)
ans = 0
maxH = max(H)
for h in range(maxH):
    state = 0
    for n in range(N+1):
        if H[n] > 0:
            H[n] -= 1
            state = 1
        elif H[n] == 0 and state == 1:
            state = 0
            ans += 1
        else:
            pass
print(ans)
