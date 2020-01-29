H,W = map(int,input().split())
grid = [input() for i in range(H)]

INF = 10 ** 18

ans = 0
for h in range(H):
    for w in range(W):
        if grid[h][w] == '#':
            continue
        dist = [[INF] * W for _ in range(H)]
        dist[h][w] = 0
        q = [(h,w)]
        d = 1
        while q:
            qq = []
            for y,x in q:
                for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                    yy,xx = y+dy, x+dx
                    if not (0 <= yy < H and 0 <= xx < W):
                        continue
                    if grid[yy][xx] == '#':
                        continue
                    if dist[yy][xx] != INF:
                        continue
                    dist[yy][xx] = d
                    qq.append((yy,xx))
            q = qq
            d += 1
        for i in range(H):
            for j in range(W):
                if dist[i][j] != INF:
                    ans = max(ans,dist[i][j])

print(ans)
 
#answer = dist[gy][gx]
#print(answer)

