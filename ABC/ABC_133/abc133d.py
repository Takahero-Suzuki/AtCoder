N = int(input())
A = list(map(lambda x:2*int(x),input().split()))

x1 = 0
for i in range(N):
    if i%2 == 0:
        x1 += A[i]
    else:
        x1 -= A[i]
    
x1 = x1//2

ans = [x1]

for i in range(N-1):
    ans.append(A[i]-ans[-1])

print(' '.join(map(str,ans)))
