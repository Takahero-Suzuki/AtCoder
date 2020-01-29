N = int(input())
 
li = [list(map(int,input().split())) for _ in range(N)]

k = 0
while li[k][2] == 0:
    k += 1
 
for x in range(101):
    for y in range(101):

        H = li[k][2]+abs(li[k][0]-x)+abs(li[k][1]-y)
        f = True

        for i in range(N):
            # CxとCyを決め打ちした後の確認は、問題文に沿った形で考える
            if li[i][2] != max(H-abs(li[i][0]-x)-abs(li[i][1]-y),0):
                f = False
                break
        if f:
            print(x,y,H)
            break
    else:
        continue
    break
 