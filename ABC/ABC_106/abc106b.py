from bisect import bisect_right
li = [105, 135, 165, 189, 195]
N = int(input())
ans = bisect_right(li,N)
print(ans)