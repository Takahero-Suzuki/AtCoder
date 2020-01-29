S=input().split('/')
for n in range(3):
    S[n]=int(S[n])
if S[0]>=2020 or (S[0]==2019 and S[1]>=5):
    print('TBD')
else:
    print('Heisei')
