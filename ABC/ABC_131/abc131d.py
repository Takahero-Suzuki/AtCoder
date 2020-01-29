N = int(input())
do = [list(map(int,input().split())) for i in range(N)]

do.sort(key=lambda x:x[1])

t = 0
ans = 'Yes'
for i in range(N):
    t += do[i][0]
    if t > do[i][1]:
        ans = 'No'
        break
print(ans)
