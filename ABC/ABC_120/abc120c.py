import collections
S = list(input())
S.append('0')
S.append('1')
S_counter = collections.Counter(S)
print((S_counter.most_common()[1][1]-1)*2)
