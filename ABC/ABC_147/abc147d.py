# 入力
N = int(input())
A = list(map(int,input().split()))

P = 10**9+7
bit = [0 for i in range(60)]

# 各bit独立に1が何個あるか数える
for a in A:
    S = bin(a)
    for j in range(1,len(S)-1):
        if S[-1*j] == '1':
            bit[j-1] += 1

# 各bitの1の個数と0の個数の積が、XOR和が1になる数字の個数と一致
ans = 0
for i,a in enumerate(bit):
    ans += a*(N-a)*(2**i)
    ans %= P

print(ans)
