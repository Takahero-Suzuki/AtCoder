S = list(input())
lS = len(S)
count = 0
for i in range(lS//2):
    if S[i] != S[-1*(i+1)]:
        count += 1
print(count)