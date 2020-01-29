A = []
B = []
for i in range(5):
    a = int(input())
    A.append(a)
    B.append((a+9)-(a+9)%10)
ans = A[0] + sum(B) - B[0]
for i in range(1,5):
    ans = min(ans, A[i] + sum(B) - B[i])
print(ans)
