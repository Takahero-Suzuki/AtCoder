N,H = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
B.append(0)
a = max(A)
B.sort()
ans = 0
while a <= B[-1] and H > 0:
    b = B.pop()
    H -= b
    ans += 1
H = max(0,H)
last = (H+a-1)//a
ans += last
print(ans)
