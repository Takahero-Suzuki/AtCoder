N,M = map(int,input().split())
drink = [list(map(int,input().split())) for n in range(N)]
drink.sort(key=lambda x: x[0])
m = 0
ans = 0
while M != 0:
    if M >= drink[m][1]:
        ans += drink[m][0]*drink[m][1]
        M -= drink[m][1]
    else:
        ans += drink[m][0]*M
        M = 0
    m += 1
print(ans)
