N,K = map(int,input().split())

if K%2 != 0:
    # modK = 0となる1以上N以下のものの直積
    ans = (N//K)**3

else:
    # 上記に加えて、modK = K/2となるものの直積
    ans = (N//K)**3 + ((N-K//2)//K+1)**3
print(ans)
