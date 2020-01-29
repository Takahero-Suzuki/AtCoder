A,B,C,D=map(int,input().split())

if A>=C:
  start=A
else:
  start=C

if B<=D:
  end=B
else:
  end=D

if start<=end:
  print(end-start)
else:
  print(0)
