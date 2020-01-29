def cumulative_sum(l):
    cumu = [0]
    s = 0
    for num in l:
        s += num
        cumu.append(s)
    return cumu

N = int(input())
A = list(map(int,input().split()))

A.sort()

C = cumulative_sum(A)

AM = [C[i+1] for i in range(N)]

'''
別解
k = 1
for i in range(N):
    AM[i] = max(AM[i],AM[max(0,i-1)])
    for j in range(max(k,i+1),N):
        if AM[i]*2 >= A[j]:
            AM[i] += A[j]
            k = j+1
        else:
            break

S = sum(A)
ans = 0
for i in range(N):
    if AM[i] == S:
        ans += 1
print(ans)
'''
ans = 1
for i in range(1,N):
    if 2*AM[-1-i] >= A[-i]:
        ans += 1
    else:
        break
print(ans)


