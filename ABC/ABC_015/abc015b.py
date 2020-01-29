N = int(input())
A = list(map(int,input().split()))
for a in A:
    if a == 0:
        N -= 1
print((sum(A)+N-1)//N)