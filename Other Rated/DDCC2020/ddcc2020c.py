H,W,K = map(int,input().split())
cake = [list(input()) for i in range(H)]
K += 1
noichigo = []
for i in range(H):
    if '#' in cake[i]:
        ichigo = 0
        K -= 1
        for j in range(W):
            if cake[i][j] == '#' and ichigo == 0:
                ichigo = 1
                cake[i][j] = K
            elif cake[i][j] == '#' and ichigo == 1:
                K -= 1
                cake[i][j] = K
            else:
                cake[i][j] = K
    else:
        noichigo.append(i)
for i in range(len(noichigo)):
    get = noichigo[0]
    want = noichigo[0]
    while get in noichigo and get < H:
        get += 1
    if get < H:
        cake[want] = cake[get]
        noichigo.pop(0)
    else:
        break
for i in range(len(noichigo)):
    get = noichigo[0]
    want = noichigo[0]
    while get in noichigo:
        get -= 1
    cake[want] = cake[get]
    noichigo.pop(0)
for h in range(H):
    ans = list(map(str, cake[h]))
    print(' '.join(ans))
