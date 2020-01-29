S = list(input())
K = int(input())
count = '1'
for n in range(K):
    if S[n] != '1':
        count = S[n]
        break
print(count)

'''
1以外がK番目以内に見つかれば、最も序盤にあるやつ
K番目まで全部1なら、答えは1
'''