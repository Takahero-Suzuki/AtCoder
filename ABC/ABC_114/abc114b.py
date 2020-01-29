S = list(map(int,list(input())))
ans = 2000
for i in range(len(S)-2):
    ans = min(ans,abs(S[i]*100+S[i+1]*10+S[i+2]-753))
print(ans)
