x=int(input())

if x%11==0:
  print(2*(x//11))
elif 1<=x%11<=6:
  print(2*(x//11)+1)
else:
  print(2*(x//11)+2)

