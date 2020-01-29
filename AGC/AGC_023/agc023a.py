def cumulative_sum(l):
    cumu = [0]
    s = 0
    for num in l:
        s += num
        cumu.append(s)
    return cumu

N = int(input())
A = list(map(int,input().split()))
S = cumulative_sum(A)
S.sort()

now = S[0]
c = 1
ans = 0
for i in range(1,N+1):
    if S[i] == now:
        c += 1

    else:
        ans += c*(c-1)//2
        c = 1
        now = S[i]
print(ans+c*(c-1)//2)
