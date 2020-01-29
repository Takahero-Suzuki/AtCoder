N,M = map(int,input().split())
sub = [list(input().split()) for i in range(M)]

wa = [0 for i in range(N)]

ac = [0 for i in range(N)]

waans = 0
acans = 0

for i in range(M):
    if sub[i][1] == 'AC' and ac[int(sub[i][0])-1] == 0:
        acans += 1
        waans += wa[int(sub[i][0])-1]
        ac[int(sub[i][0])-1] = 1
    elif sub[i][1] == 'WA' and ac[int(sub[i][0])-1] == 0:
        wa[int(sub[i][0])-1] += 1

print(acans,waans)
