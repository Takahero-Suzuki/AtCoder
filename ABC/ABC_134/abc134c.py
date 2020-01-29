import copy
N = int(input())
A = [int(input()) for i in range(N)]
B = A.copy()
B.sort()
M,m = B[-1],B[-2]
for a in A:
    print(M if a != M else m)
