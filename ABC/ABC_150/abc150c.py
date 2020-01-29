import itertools

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

li = [i+1 for i in range(N)]

a = 0
b = 0
for v in itertools.permutations(li, N):
    a += 1
    b += 1
    aaa = 1
    bbb = 1
    for i in range(N):
        if v[i] != P[i]:
            aaa = 0
            break
    if aaa == 1:
        ansa = a
    for i in range(N):
        if v[i] != Q[i]:
            bbb = 0
            break
    if bbb == 1:
        ansb = b
print(abs(ansa-ansb))
