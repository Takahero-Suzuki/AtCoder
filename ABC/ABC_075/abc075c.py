from collections import deque

N,M = map(int,input().split())
sides = [list(map(int,input().split())) for i in range(M)]

vertex = [[] for i in range(N)]
for side in sides:
    vertex[side[0]-1].append(side[1])
    vertex[side[1]-1].append(side[0])

# print(vertex)

ans = 0

for side in sides:
    vertex[side[0]-1].remove(side[1])
    vertex[side[1]-1].remove(side[0])
    # print(vertex)
    for i in range(1,N+1):
        a = 1
        check = deque([i])
        fromcheck = {j:0 for j in range(1,N+1)}
        visit = {i}
        while len(check) != 0:
            v = check.popleft()
            for ver in vertex[v-1]:
                if fromcheck[ver] == 0:
                    fromcheck[ver] = 1
                    check.append(ver)
                    visit.add(ver)
            fromcheck[v] = 1
        if visit != {i for i in range(1,N+1)}:
            a = 0
            break
    if a == 0:
        ans += 1
    vertex[side[0]-1].append(side[1])
    vertex[side[1]-1].append(side[0])

print(ans)
