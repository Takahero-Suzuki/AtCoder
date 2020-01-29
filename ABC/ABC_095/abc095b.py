N,X = map(int,input().split())
donut_count = 0
cheep_donut = 1001
for n in range(N):
    donut = int(input())
    X -= donut
    donut_count += 1
    if donut < cheep_donut:
        cheep_donut = donut
while X >= cheep_donut:
    donut_count += 1
    X -= cheep_donut

print(donut_count)
