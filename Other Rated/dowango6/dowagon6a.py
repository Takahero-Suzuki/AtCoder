N = int(input())
st = [list(input().split()) for i in range(N)]
X = input()

#print(st)
suma = 0

T = 0

for i in range(N):
    if T == 1:
        suma += int(st[i][1])
    if st[i][0] == X:
        T = 1

print(suma)