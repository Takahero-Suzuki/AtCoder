S = list(input())
N = int(input())
for n in range(N):
    l,r = map(int,input().split())
    Sb = S[:l-1]
    Sa = S[r:]
    Sc = S[l-1:r:]
    Sc.reverse()
    S = Sb + Sc + Sa
print(''.join(S))
