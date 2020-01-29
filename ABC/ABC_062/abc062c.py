H,W = map(int,input().split())

S = H*W
ans = 10**10

hs = H//2
ws = W//2

for h in range(1,hs+1):
    a = h*W
    if (H-h)%2 == 0 or W%2 == 0:
        b = (S-a)//2
    else:
        b = min(H-h,W)*(max(H-h,W)//2)
    c = S-a-b
    d = max(a,b,c)-min(a,b,c)
    ans = min(ans,d)

for w in range(1,ws+1):
    a = H*w
    if (W-w)%2 == 0 or H%2 == 0:
        b = (S-a)//2
    else:
        b = min(W-w,H)*(max(W-w,H)//2)
    c = S-a-b
    d = max(a,b,c)-min(a,b,c)
    ans = min(ans,d)

print(ans)
