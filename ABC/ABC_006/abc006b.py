N = int(input())
a = [0,0,1]

P = 10**4+7
for i in range(N-3):
    a.append((a[-1]+a[-2]+a[-3])%P)
print(a[N-1])
