from bisect import bisect_left

N,M = map(int,input().split())
PtoY = [[] for n in range(N)]
check = []

for m in range(M):
    P,Y = map(int,input().split())
    PtoY[P-1].append(Y)
    check.append([P,Y])

for n in range(N):
    PtoY[n].sort()

for m in range(M):
    p,y = check[m][0],check[m][1]
    a = bisect_left(PtoY[p-1],y)+1
    string = str(p).zfill(6) + str(a).zfill(6)
    print(string)
