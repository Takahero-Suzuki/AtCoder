'''
X = list(map(int,input().split()))
ans = 0
for x in X:
    if x == 1:
        ans += 300000
    elif x == 2:
        ans += 200000
    elif x == 3:
        ans += 100000
if ans == 600000:
    ans += 400000
print(ans)
'''
X,Y = map(int,input().split())
if X*Y == 1:
    print(10**6)
else:
  print(10**5*(max(0,4-X)+max(0,4-Y)))
