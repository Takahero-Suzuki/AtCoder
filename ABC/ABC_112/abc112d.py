from bisect import bisect_right

def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    ass.sort()
    return ass 

N,M = map(int,input().split())
a = M//N

li = divisor(M)

x = bisect_right(li,a)

print(li[x-1])
