import math
N = int(input())
rootN = int(math.sqrt(N))
while N%rootN != 0:
    rootN -= 1
print(len(str(N//rootN)))