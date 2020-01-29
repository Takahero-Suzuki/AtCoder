import collections

N,M = map(int,input().split())
A = list(map(int,input().split()))
bc = [list(map(int,input().split())) for i in range(M)]

card = collections.Counter(A).most_common()

card.sort(key=lambda x: x[0])
bc.sort(key=lambda x: x[1])

#print(card)
#print(bc)

ans = 0

while N != 0 and len(card) != 0 and len(bc) != 0:
    if card[-1][0] >= bc[-1][1]:
        x = card.pop()
        ans += x[0]*min(x[1],N)
        N = max(N-x[1],0)
    else:
        x = bc.pop()
        ans += x[1]*min(x[0],N)
        N = max(N-x[0],0)

if N != 0:
    if len(card) == 0:
        while N != 0:
            x = bc.pop()
            ans += x[1]*min(x[0],N)
            N = max(N-x[0],0)
    else:
        while N != 0:
            x = card.pop()
            ans += x[0]*min(x[1],N)
            N = max(N-x[1],0)

print(ans)
