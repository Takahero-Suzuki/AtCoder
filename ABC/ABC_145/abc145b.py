N = int(input())
S = list(input())
if N%2 == 0:
    judge = 'Yes'
    for n in range(N//2):
        if S[n] != S[n+N//2]:
            judge = 'No'
            break
else:
    judge = 'No'
print(judge)



        