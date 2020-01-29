#0-originなので座標は全て-1してから使うこと！
#グリッドBFS
def gridbfs(grid,sy,sx):
    INF = 10**18

    gridy = len(grid)
    gridx = len(grid[0])

    dist = [[INF]*gridx for _ in range(gridy)]
    dist[sy][sx] = 0
    q = [(sy,sx)]
    d = 1

    while q:
        qq = []
        for y,x in q:
            for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                yy,xx = y+dy, x+dx
                if not (0 <= yy < gridy and 0 <= xx < gridx):
                    continue
                if grid[yy][xx] == '#':
                    continue
                if dist[yy][xx] != INF:
                    continue
                dist[yy][xx] = d
                qq.append((yy,xx))
        q = qq
        d += 1

    return dist

H,W = map(int,input().split())
grid = [input() for i in range(H)]
d = gridbfs(grid,0,0)
b = 0
for h in range(H):
    for w in range(W):
        if grid[h][w] == '#':
            b += 1

print(max(H*W-b-d[H-1][W-1]-1,-1))
'''
3 3
..#
##.
...
'''