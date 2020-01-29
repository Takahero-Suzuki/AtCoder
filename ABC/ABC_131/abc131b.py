N,L = map(int,input().split())

aji = [L+i for i in range(N)]
s = sum(aji)
m = aji[0]
for i in range(N):
    if abs(m) > abs(aji[i]):
        m = aji[i]
print(s-m)
