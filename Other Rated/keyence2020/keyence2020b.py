N = int(input())
XL = [list(map(int,input().split())) for i in range(N)]
XL.sort(key=lambda x: x[0]+x[1])
M = XL[0][0]+XL[0][1]-1
ans = 0
for i in range(1,N):
    if M >= XL[i][0]-XL[i][1]:
        ans += 1
    else:
        M = XL[i][0]+XL[i][1]-1
print(N-ans)
