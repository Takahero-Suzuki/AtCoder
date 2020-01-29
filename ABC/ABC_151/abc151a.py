c = input()
li = [chr(i) for i in range(97,97+26)]

for i in range(26):
    if c == li[i]:
        print(li[i+1])
        break

c = input()
print(chr(ord(c)+1))