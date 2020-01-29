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

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
c = [input() for _ in range(R)]

print(gridbfs(c,sy-1,sx-1)[gy-1][gx-1])

