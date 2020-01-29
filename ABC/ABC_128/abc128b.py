N = int(input())

S = [input().split() +[_+1] for _ in range(N)]

for i in range(N):
    S[i][1] = int(S[i][1])

S.sort(key=lambda x: x[0])

now = S[0][0]
pre = []

for i in range(N):
    if now == S[i][0]:
        pre.append(S[i])
    else:
        pre.sort(key=lambda x: x[1],reverse=True)
        for j in range(len(pre)):
            print(pre[j][2])
        pre = [S[i]]
        now = S[i][0]

pre.sort(key=lambda x: x[1],reverse=True)
for j in range(len(pre)):
    print(pre[j][2])
