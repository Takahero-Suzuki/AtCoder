import collections
N = int(input())
V = list(map(int,input().split()))
V_even = V[::2]
V_odd = V[1::2]
V_even_counter = collections.Counter(V_even)
V_odd_counter = collections.Counter(V_odd)
if V_even_counter.most_common()[0][0] != V_odd_counter.most_common()[0][0]:
    ans = N - V_even_counter.most_common()[0][1] - V_odd_counter.most_common()[0][1]
else:
    if len(V_even_counter) > 1 and len(V_odd_counter) > 1:
        ans = N - max(V_even_counter.most_common()[0][1] + V_odd_counter.most_common()[1][1],\
            V_even_counter.most_common()[1][1] + V_odd_counter.most_common()[0][1])
    elif len(V_even_counter) == 1 and len(V_odd_counter) > 1:
        ans = N - V_even_counter.most_common()[0][1] - V_odd_counter.most_common()[1][1]
    elif len(V_even_counter) > 1 and len(V_odd_counter) == 1:
        ans = N - V_even_counter.most_common()[1][1] + V_odd_counter.most_common()[0][1]
    else:
        ans = N//2
print(ans)
