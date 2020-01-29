S=list(input())
l=0
while l!=len(S):
  l=len(S)
  if S[-1]=='m' and S[-2]=='a' and S[-3]=='e' and S[-4]=='r' and S[-5]=='d':
    del S[-5:]
  if len(S)==0:
    break
  if S[-1]=='e' and S[-2]=='s' and S[-3]=='a' and S[-4]=='r' and S[-5]=='e':
    del S[-5:]
  if len(S)==0:
    break
  if S[-1]=='r' and S[-2]=='e' and S[-3]=='s' and S[-4]=='a' and S[-5]=='r' and S[-6]=='e':
    del S[-6:]
  if len(S)==0:
    break
  if S[-1]=='r' and S[-2]=='e' and S[-3]=='m' and S[-4]=='a' and S[-5]=='e' and S[-6]=='r' and S[-7]=='d':
    del S[-7:]
  if len(S)==0:
    break

if len(S)==0:
  print('YES')
else:
  print('NO')
