N = int(input())
S = input()

cr = 0
cl = 0

for i in range(N):
    if S[i] == '(':
        cr += 1
    else:
        if cr > 0:
            cr -= 1
        else:
            cl += 1
print('('*cl+S+')'*cr)
