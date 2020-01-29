N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
s = 10000
ans = 0
for i,h in enumerate(H,1):
    if abs(T-h*0.006-A) < s:
        s = abs(T-h*0.006-A)
        ans = i
print(ans)
