N,M=map(int,input().split())
if min(N,M)>=2:
    print((N-2)*(M-2))
elif N*M==1:
    print(1)
else:
    print(max(N,M)-2)
