N,Q = map(int,input().split())
S = list(input())
ac_counter = [0]
counter = 0
for i in range(1,N):
    if S[i-1] == 'A' and S[i] == 'C':
        counter += 1
    ac_counter.append(counter)
for j in range(Q):
    l,r = map(int,input().split())
    print(ac_counter[r-1]-ac_counter[l-1])
