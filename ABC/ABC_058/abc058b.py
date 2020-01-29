O = list(input())
E = list(input())
ans = []
for i in range(len(O)+len(E)):
    if i%2 == 0:
        ans.append(O[i//2])
    else:
        ans.append(E[i//2])
print(''.join(ans))