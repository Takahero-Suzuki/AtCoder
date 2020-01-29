N = int(input())
A = list(map(int,input().split()))
ans = sum(A)-N
print(ans)

'''
すべての数の積mは当然すべての数に対しm moda_n=0なので
(m-1)moda_n=a_n　-　1となる
'''
