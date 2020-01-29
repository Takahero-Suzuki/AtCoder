A,B,C,D,E,F = map(int,input().split())
f = F//100

ans = [0,0]
per = -1

for w in range(1,f+1):
    wt = 0
    for b in range(0,w+1,B):
        if (w-b)%A == 0:
            wt = 1
            break
    if wt == 0:
        continue
    water = w*100

    for s in range(min(w*E,F-water),-1,-1):
        st = 0
        for d in range(0,s+1,D):
            if (s-d)%C == 0:
                st = 1
                break
        if st == 1:
            break

    if s/(s+water) > per:
        ans = [s+water,s]
        per = s/(s+water)

print(' '.join(map(str,ans)))
