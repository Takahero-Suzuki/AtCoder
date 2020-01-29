N,A,B=map(int,input().split())
if A==B:
  print(1)
else:
  if N==1:
    print(0)
  else:
    if A<B:
      print((N-2)*(B-A)+1)
    else:
      print(0)
      