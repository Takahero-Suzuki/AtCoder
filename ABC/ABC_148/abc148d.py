N = int(input())
a = list(map(int,input().split()))
R = 1
for i in range(N):
    if a[i] == R:
        R += 1
print(N-R+1 if R != 1 else -1)

