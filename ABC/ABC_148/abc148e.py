N = int(input())
if N%2 != 0:
    ans = 0
else:
    ans = 0
    for i in range(1,1000):
        ans += N//(2*(5**i))
print(ans)

