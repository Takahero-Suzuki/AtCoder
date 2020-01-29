S = list(input())
odd_zero = 0
even_zero = 0
odd_one = 0
even_one = 0
for n in range(len(S)):
    if n%2 == 0:
        if S[n] == '0':
            even_zero += 1
        else:
            even_one += 1
    else:
        if S[n] == '0':
            odd_zero += 1
        else:
            odd_one += 1
print(len(S)-max(even_zero+odd_one, even_one+odd_zero))
