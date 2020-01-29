N = int(input())
p = list(map(int,input().split()))

notsame = 0
for i in range(N):
    if p[i] != i+1:
        notsame += 1
print('YES' if notsame == 2 or notsame == 0 else 'NO')
