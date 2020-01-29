N=int(input())
name_dict={'M':0,'A':0,'R':0,'C':0,'H':0}
for n in range(N):
    S=list(input())
    if S[0] in name_dict:
        name_dict[S[0]]+=1

ans=name_dict['M']*name_dict['A']*name_dict['R']\
    +name_dict['M']*name_dict['A']*name_dict['C']\
    +name_dict['M']*name_dict['A']*name_dict['H']\
    +name_dict['M']*name_dict['R']*name_dict['C']\
    +name_dict['M']*name_dict['R']*name_dict['H']\
    +name_dict['M']*name_dict['C']*name_dict['H']\
    +name_dict['A']*name_dict['R']*name_dict['C']\
    +name_dict['A']*name_dict['R']*name_dict['H']\
    +name_dict['A']*name_dict['C']*name_dict['H']\
    +name_dict['R']*name_dict['C']*name_dict['H']
print(ans)
