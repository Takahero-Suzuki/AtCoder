def nbasesum(value,n):
    nbasevalue = 0
    while value > 0:
        nbasevalue += value%n
        value //= n
    return nbasevalue

N = int(input())
ans = nbasesum(N,9)

for i in range(N+1):
    c6 = i
    c9 = N-i
    ans = min(ans, nbasesum(c9,9)+nbasesum(c6,6))

print(ans)
