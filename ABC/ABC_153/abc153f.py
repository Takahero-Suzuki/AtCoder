from collections import deque

N,D,A = map(int,input().split())
mons = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    mons[i][1] = (mons[i][1]+A-1)//A

mons.sort(key=lambda x: x[0])

damages = deque()
nowdmg = 0
ans = 0
for i in range(N):
    while len(damages) != 0:
        if mons[i][0] >= damages[0][0]+1:
            rec = damages.popleft()
            nowdmg += rec[1]
        else:
            break
    if mons[i][1]+nowdmg > 0:
        c = mons[i][1]+nowdmg
        ans += c
        damages.append([mons[i][0]+2*D,c])
        nowdmg -= c

print(ans)
