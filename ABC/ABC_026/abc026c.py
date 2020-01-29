N = int(input())

wker = [[] for i in range(N+1)]

for i in range(2,N+1):
    b = int(input())
    wker[b].append(i)
#print(wker)

f = [[0,False] for _ in range(N+1)]
f[0][1] = True

for i in range(1,N+1):
    if wker[i] == []:
        f[i][0] = 1
        f[i][1] = True
#print(f)

c = False

while c == False:
    for i in range(1,N+1):
        d = True
        for j in wker[i]:
            if f[j][1] == False:
                d = False
                break
        if d == True and not f[i][0]:
            m = 10**7
            M = 0
            for j in wker[i]:
                M = max(f[j][0],M)
                m = min(f[j][0],m)
            f[i][0] = M+m+1
            f[i][1] = True
    d = True
    for i in range(1,N+1):
        if f[i][1] == False:
            d = False
    if d == True:
        c = True

#print(f)

print(f[1][0])

        