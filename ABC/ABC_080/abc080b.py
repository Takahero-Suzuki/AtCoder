N=int(input())
N_sum=list(str(N))
fN=0
for n in range(len(N_sum)):
  fN+=int(N_sum[n])
if N%fN==0:
  print('Yes')
else:
  print('No')
