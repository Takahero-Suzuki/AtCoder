N = int(input())
S = input()
ans = 0
snumber = [str(i) for i in range(10)]
for i in snumber:
    for j in snumber:
        for k in snumber:
            a = S.find(i)
            if a == -1:
                break
            b = S.find(j,a+1)
            if b == -1:
                break
            c = S.find(k,b+1)
            if c != -1:
                ans += 1
print(ans)

'''
PyPy3で通り、Python3だとTLE
N = int(input())
S = list(input())
ans = 0
snumber = [str(i) for i in range(10)]
for i in snumber:
    for j in snumber:
        for k in snumber:
            n = 0
            while i != S[n] and n < N-3:
                n += 1
            if S[n] != i:
                break
            n += 1
            while j != S[n] and n < N-2:
                n += 1
            if S[n] != j:
                break
            n += 1
            while k != S[n] and n < N-1:
                n += 1
            if S[n] == k:
                ans += 1
print(ans)
'''