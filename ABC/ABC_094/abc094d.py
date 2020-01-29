import bisect
n = int(input())
a = list(map(int,input().split()))

a.sort()

ai = a[-1]

ind = bisect.bisect_left(a,ai//2+1)

if a[ind-1] < ai-a[ind]:
    aj = a[ind]
else:
    aj = a[ind-1]

print(ai,aj)
