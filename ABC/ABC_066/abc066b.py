S=list(input())
lenS=len(S)
ans=0

if lenS%2==0:
  for l in range(lenS//2-1):
    check=0
    for k in range(l+1):
      if S[k]==S[k+l+1]:
        check+=1
    if check==l+1:
      ans=check*2
  print(ans)

else:
  for l in range(lenS//2):
    check=0
    for k in range(l+1):
      if S[k]==S[k+l+1]:
        check+=1
    if check==l+1:
      ans=check*2
  print(ans)

  