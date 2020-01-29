N = int(input())
shiritori = []
ans = 'Yes'
w = input()
last = w[-1]
shiritori.append(w)
for i in range(N-1):
    w = input()
    if w in shiritori:
        ans = 'No'
        break
    elif last != w[0]:
        ans = 'No'
        break
    else:
        last = w[-1]
        shiritori.append(w)
print(ans)
