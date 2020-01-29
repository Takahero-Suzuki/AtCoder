S = list(input())

even = ['R','U','D']
odd = ['L','U','D']
ans = 'Yes'
for i in range(len(S)):
    if (i%2 == 0 and S[i] not in even) or (i%2 == 1 and S[i] not in odd):
        ans = 'No'
        break
print(ans)
