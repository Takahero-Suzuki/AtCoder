a,b,x = map(int,input().split())

def bisect(A,B,X):
    L = 1
    R = 10**9
    while L < R:
        mid = (L+R)//2
        if A*mid + B*len(str(mid)) <= X and A*(mid+1) + B*len(str(mid+1)) > X:
            return mid
        elif A*mid + B*len(str(mid)) > X:
            R = mid
        else:
            L = mid+1

if a*10**9 + b*10 <= x:
    ans = 10**9
elif a + b > x:
    ans = 0
else:
    ans = bisect(a,b,x)
print(ans)


