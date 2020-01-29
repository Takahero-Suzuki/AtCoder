N = int(input())
a = [int(input()) for n in range(N)]
sorted_a = sorted(set(a))
i_index = {num:i for i,num in enumerate(sorted_a)}
for i in a:
    print(i_index[i])

'''
～別解～
from bisect import bisect_left
N = int(input())
a = [int(input()) for n in range(N)]
sorted_a = sorted(set(a))
for i in a:
    print(bisect_left(sorted_a,i))
'''
