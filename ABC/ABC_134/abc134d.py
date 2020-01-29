N = int(input())
a = list(map(int,input().split()))

b = [0 for i in range(N//2)]+a[N//2:]

for i in range(N//2-1,-1,-1):
    if sum(b[i::i+1])%2 == 0:
        b[i] = a[i]
    else:
        b[i] = 1-a[i]

ans = []
for i in range(N):
    if b[i] == 1:
        ans.append(i+1)

print(len(ans))
print(' '.join(map(str,ans)))
