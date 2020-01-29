N,M,W=map(int,input().split())

goods_list=[]
for n in range(N):
  good=list(map(int,input().split()))	
  goods_list.append(good)

# 二次元配列の重複を取り除く関数を定義
def get_unique_list(seq):
    seen=[]
    return [x for x in seq if x not in seen and not seen.append(x)]

# mは0かそれ以外で場合分けする
if M!=0:
  marge_list=[]
  for m in range(M):
    marge=list(map(int,input().split()))
    marge.sort()
    marge_list.append(marge)

  for m in range(M):
    a=marge_list[m][0]-1
    b=marge_list[m][1]-1
    goods_list[a][0]+=goods_list[b][0]
    goods_list[a][1]+=goods_list[b][1]
    goods_list[b]=goods_list[a]

  ans_goods_list=get_unique_list(goods_list)

else:
  ans_goods_list=goods_list

N=len(ans_goods_list)

dp=[[0 for i in range(W+1)] for j in range(N+1)]

w=[]
v=[]
for i in range(N):
  x=ans_goods_list[i][0]
  y=ans_goods_list[i][1]
  w.append(x)
  v.append(y)

for i in range(N-1,-1,-1):
    for j in range(W+1):
        if j<w[i]:
            dp[i][j]=dp[i+1][j]
        else:
            dp[i][j]=max(dp[i+1][j],dp[i+1][j-w[i]]+v[i])

print(dp[0][W])

