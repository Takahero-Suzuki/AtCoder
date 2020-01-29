N = int(input())
H = list(map(int,input().split()))
ans = 0
now = H[0]
count = 0
for i in range(1,N):
    if now >= H[i]:
        count += 1
        now = H[i]
    else:
        now = H[i]
        ans = max(ans,count)
        count = 0
ans = max(ans,count)
print(ans)
