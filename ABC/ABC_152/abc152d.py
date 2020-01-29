N = int(input())

li = [[0 for j in range(9)] for i in range(9)]

for i in range(1,N+1):
    start = str(i)[0]
    end = str(i)[-1]
    if start != '0' and end != '0':
        li[int(start)-1][int(end)-1] += 1
ans = 0
for i in range(1,N+1):
    start = str(i)[0]
    end = str(i)[-1]
    if start != '0' and end != '0':
        ans += li[int(end)-1][int(start)-1]
print(ans)