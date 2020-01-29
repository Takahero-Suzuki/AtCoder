H,N = map(int,input().split())
A = list(map(int,input().split()))
if H <= sum(A):
    print('Yes')
else:
    print('No')


'''
H,N = map(int,input().split())
magic = [list(map(int,input().split())) for i in range(N)]

print(magic)

P = [[magic[i][0]/magic[i][1],i] for i in range(N)]

print(P)

P.sort(key=lambda x: x[0])

print(P)
ans = 0
while H > 0 and len(P) != 0:
    p = P.pop()
    a = magic[p[1]][0]
    b = magic[p[1]][1]
    t = H//a
    H -= a*t
    ans += b*t
if H != 0:
    magic.sort(key=lambda x: x[1])
    ans += magic[0][1]

print(ans)


'''