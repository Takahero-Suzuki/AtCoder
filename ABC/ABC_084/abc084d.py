def primes(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    return is_prime

e = primes(10**5)

tc = 0
li = []

for i in range(len(e)):
    if i%2 == 0:
        li.append(tc)
    else:
        if e[i] and e[(i+1)//2]:
            tc += 1
        li.append(tc)

Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    print(li[r]-li[l-1])
