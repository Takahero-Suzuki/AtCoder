from collections import Counter
N = int(input())
r = list(input())
rcounter = Counter(r)
ans = 0
ans += rcounter['A']*4
ans += rcounter['B']*3
ans += rcounter['C']*2
ans += rcounter['D']*1
ans += rcounter['F']*0
print(ans/N)