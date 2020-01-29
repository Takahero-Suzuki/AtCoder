N=int(input())

for n in range(7):
  if 2**(n)<=N<2**(n+1):
    print(2**(n))
