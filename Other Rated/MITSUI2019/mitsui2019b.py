N = int(input())
x1 = N//1.08
x2 = x1 + 1
if int(x1*1.08) == N:
    print(int(x1))
elif int(x2*1.08) == N:
    print(int(x2))
else:
    print(':(')
