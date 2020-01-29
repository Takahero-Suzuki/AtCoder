import copy
N = int(input())
H = list(map(int,input().split()))
ans = 'Yes'
H2 = H.copy()
for n in range(N):
    H2[n] -= 1
H3 = [H2[0]]
for n in range(1,N):
    if H3[-1] <= H2[n]:
        H3.append(H2[n])
    elif H3[-1] <= H[n]:
        H3.append(H[n])
    else:
        ans = 'No'
        break
print(ans)
'''
for n in range(N-1):
    if H[n] > H[n+1]:
        H[n] -= 1
for n in range(N-1):
    if H[n] > H[n+1]:
        ans = 'No'
        break
print(ans)
'''
'''
hM,hm = H[0],H[0]-1
for n in range(1,N):
    if H[n] >= hM:
        hM,hm = H[n],H[n]-1
    elif H[n] >= hm:
        hM = hm
    else:
        ans = 'No'
        break
print(ans)
'''