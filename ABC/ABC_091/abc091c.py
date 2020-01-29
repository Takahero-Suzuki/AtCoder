N = int(input())
AB = [list(map(int,input().split())) for i in range(N)]
CD = [list(map(int,input().split())) for i in range(N)]

AB.sort()
CD.sort()

#print(AB)
#print(CD)

ans = 0
'''
for cd in CD:
    li = []
    for ab in AB:
        if ab[0] < cd[0] and ab[1] < cd[1]:
            li.append(ab)
    li.sort(key=lambda x: x[1])
    if len(li) != 0:
        AB.remove(li[-1])
        ans += 1

print(ans)
'''

for i in range(N-1,-1,-1):
    ab = AB[i]
    li = []
    for cd in CD:
        if ab[0] < cd[0] and ab[1] < cd[1]:
            li.append(cd)
    li.sort(key=lambda x: x[1])
    if len(li) != 0:
        CD.remove(li[0])
        ans += 1
print(ans)
