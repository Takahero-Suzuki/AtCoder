N = int(input())
S = sum(list(map(int,str(N))))
if N%S == 0:
    print('Yes')
else:
    print('No')
