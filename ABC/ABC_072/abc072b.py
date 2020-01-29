# 切り上げ：(a+1)//2
s=list(input())
lens=len(s)
l=(lens+1)//2
ans=[]

for n in range(l):
  ans.append(s[2*n])

print(''.join(ans))