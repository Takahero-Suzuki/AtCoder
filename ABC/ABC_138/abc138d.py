#PyPy3のみAC(Python3ではTLE)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
from collections import deque
 
N,Q = map(int,readline().split())
ki = []
for i in range(N-1):
    ki.append(list(map(int,readline().split())))
co = []
for i in range(Q):
    co.append(list(map(int,readline().split())))
 
ki.sort(key=lambda x: x[1])
 
kid = deque(ki)
ver = []
check = []
for i in range(N):
    ver.append(0)
    check.append(False)
 
for c in co:
    ver[c[0]-1] += c[1]
 
check[0] = True
 
kid2 = deque()
 
while len(kid) != 0:
    k = kid.popleft()
    if check[k[0]-1] == True:
        ver[k[1]-1] += ver[k[0]-1]
        check[k[1]-1] = True
    elif check[k[1]-1] == True:
        ver[k[0]-1] += ver[k[1]-1]
        check[k[0]-1] = True
    else:
        kid2.append(k)
 
while len(kid2) != 0:
    k = kid2.pop()
    if check[k[0]-1] == True:
        ver[k[1]-1] += ver[k[0]-1]
        check[k[1]-1] = True
    elif check[k[1]-1] == True:
        ver[k[0]-1] += ver[k[1]-1]
        check[k[0]-1] = True
    else:
        kid2.appendleft(k)
