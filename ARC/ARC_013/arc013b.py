C = int(input())
m1 = 0
m2 = 0
m3 = 0
for i in range(C):
    M = list(map(int,input().split()))
    M.sort()
    m1 = max(m1,M[0])
    m2 = max(m2,M[1])
    m3 = max(m3,M[2])
print(m1*m2*m3)
