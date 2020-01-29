N = int(input())
capacity = [int(input()) for i in range(5)]
ans = 5+(N-1)//min(capacity) 
print(ans)
