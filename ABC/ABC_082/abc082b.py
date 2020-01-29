ls=list(input())
lt=list(input())
if ls!=lt:
  ls.sort()
  lt.sort(reverse=True)
  s_sorted=''.join(ls)
  t_sorted=''.join(lt)
  before=[s_sorted,t_sorted]
  after=[s_sorted,t_sorted]
  after.sort()
  if before==after:
    print('Yes')
  else:
    print('No')

else:
  print('No')
