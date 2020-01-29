H,W = map(int,input().split())
campus = [list(input()) for h in range(H)]

ans = 1
for h in range(H):
    for w in range(W):
        if campus[h][w] == '#':
            check = 0
            if h != 0:
                if campus[h-1][w] == '#':
                    check = 1
            if w != 0:
                if campus[h][w-1] == '#':
                    check = 1
            if h != H-1:
                if campus[h+1][w] == '#':
                    check = 1
            if w != W-1:
                if campus[h][w+1] == '#':
                    check =1
            if check == 0:
                ans = 0
                break

if ans == 1:
    print('Yes')
else:
    print('No')
