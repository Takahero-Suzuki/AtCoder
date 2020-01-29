A,B=map(int,input().split())
S=list(input())
count=0
for n in range(A):
  if S[n]!='-':
    count+=1
  else:
    break
if S[A]=='-':
  count+=1
for n in range(A+1,A+B+1):
  if S[n]!='-':
    count+=1
  else:
    break
if count==A+B+1:
  print('Yes')
else:
  print('No')


