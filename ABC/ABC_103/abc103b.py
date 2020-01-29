S = list(input()*2)
T = list(input())
ans = 'No'
for i in range(len(S)//2):
    check = 1
    for j in range(len(S)//2):
        if S[i+j] != T[j]:
            check = 0
    if check == 1:
        ans = 'Yes'
        break
print(ans)
