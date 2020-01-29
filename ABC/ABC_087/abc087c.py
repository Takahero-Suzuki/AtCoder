N=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
M=sum(A2)+A1[0]
now=M
for n in range(N-1):
  now=now+A1[n+1]-A2[n]
  if M<now:
    M=now
print(M)
