S = input()

a = S[0]+S[1]
b = S[2]+S[3]

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

if a in month and b in month:
    ans = 'AMBIGUOUS'
elif a in month:
    ans = 'MMYY'
elif b in month:
    ans = 'YYMM'
else:
    ans = 'NA'

print(ans)
