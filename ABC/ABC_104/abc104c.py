import itertools

D,G = map(int,input().split())
pc = [list(map(int,input().split())) for i in range(D)]
print(pc)

ans = 10**5

for v in itertools.product([0,1],repeat=D):
    p = 0
    t = 0
    for i in range(D):
        if v[i] == 1:
            p += (i+1)*100*pc[i][0] + pc[i][1]
            t += pc[i][0]
    #print(v)
    #print(p)
    w = G-p
    if w > 0:
        for i in range(D):
            if v[i] == 0 and w <= (i+1)*100*(pc[i][0]-1):
                a = (i+1)*100
                tt = t+(w+a-1)//a
                ans = min(ans,tt)
    else:
        ans = min(ans,t)
print(ans)
