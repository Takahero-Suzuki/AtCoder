n = -2
N = int(input())
ans = 0
digit = 0
while N != 0:
    if N%2 == 0:
        N //= n
        digit += 1
    else:
        ans += 1*(10**digit)
        N = N//n + 1
        digit += 1
print(ans)

'''
print(-9//n)
print(-9%n)
print(-11//n)
print(-11%n)
print(5//n)
print(5%n)
print(3//n)
print(3%n)
print(-2//n)
print(-2%n)
print(-1//n)
print(-1%n)
print(1//n)
print(1%n)
'''