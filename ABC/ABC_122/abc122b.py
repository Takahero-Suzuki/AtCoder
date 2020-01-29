S = list(input())
acgt = ['A', 'C', 'G', 'T']
ans = 0
for i in range(len(S)+1):
    for j in range(i):
        A = S[j:i]
        T = 1
        for a in A:
            if a not in acgt:
                T = 0
                break
        if T == 1:
            ans = max(ans,len(A))
print(ans)