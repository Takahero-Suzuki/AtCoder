H,W = map(int,input().split())
g = [list(input()) for i in range(H)]
 
c = [[0 for w in range(W)] for h in range(H)]
 
hs = [0 for i in range(W)]
 
for h in range(H):
    ws = 0
    for w in range(W):
        if g[h][w] == '#':
            for i in range(ws,w):
                c[h][i] += w-ws-1
            ws = w+1
            for j in range(hs[w],h):
                c[j][w] += h-hs[w]
            hs[w] = h+1
    w2 = w+1
    for i in range(ws,w2):
        c[h][i] += w2-ws-1
h2 = h+1
for w in range(W):
    for j in range(hs[w],h2):
        c[j][w] += h2-hs[w]
 
#print(c)
 
ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans,c[h][w])
 
print(ans)
'''
横方向と縦方向に分けてプログラムを作成してまとめた
横方向
for h in range(H):
    ws = 0
    for w in range(W):
        if g[h][w] == '#':
            for i in range(ws,w):
                c[h][i] += w-ws-1
            ws = w+1
    w2 = w+1
    for i in range(ws,w2):
        c[h][i] += w2-ws-1
 
縦方向
hs = [0 for i in range(W)]
for h in range(H):
    for w in range(W):
        if g[h][w] == '#':
            for j in range(hs[w],h):
                c[j][w] += h-hs[w]
            hs[w] = h+1
h2 = h+1
for w in range(W):
    for j in range(hs[w],h2):
        c[j][w] += h2-hs[w]
'''