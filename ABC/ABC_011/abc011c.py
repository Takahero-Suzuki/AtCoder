N = int(input())
NG = [int(input()) for _ in range(3)]
if N in NG:
    ans = 'NO'
else:
    c = 0
    T = True
    while T:
        if N-3 not in NG and N-3 >= 0:
            N -= 3
            c += 1
        elif N-2 not in NG and N-2 >= 0:
            N -= 2
            c += 1
        elif N-1 not in NG and N-1 >= 0:
            N -= 1
            c += 1
        else:
            T = False
    if c <= 100 and N == 0:
        ans = 'YES'
    else:
        ans = 'NO'

print(ans)
