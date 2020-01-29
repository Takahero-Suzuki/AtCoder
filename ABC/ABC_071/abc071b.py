S=list(input())

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','None']

S.sort()

for s in alphabet:
  if s in S:
    pass
  else:
    print(s)
    break
