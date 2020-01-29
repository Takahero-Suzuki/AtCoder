N = int(input())
name = 'atcoder'
people = 0
S = 0
for n in range(N):
    s,p = input().split()
    p = int(p)
    if p > people:
        people = p
        name = s
    S += p
if people >  S/2:
    print(name)
else:
    print('atcoder')
