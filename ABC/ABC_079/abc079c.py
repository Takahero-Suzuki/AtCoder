li=list(input())
A=int(li[0])
B=int(li[1])
C=int(li[2])
D=int(li[3])
if A+B+C+D==7:
  print(li[0]+'+'+li[1]+'+'+li[2]+'+'+li[3]+'=7')
  
elif A+B+C-D==7:
  print(li[0]+'+'+li[1]+'+'+li[2]+'-'+li[3]+'=7')
  
elif A+B-C+D==7:
  print(li[0]+'+'+li[1]+'-'+li[2]+'+'+li[3]+'=7')

elif A+B-C-D==7:
  print(li[0]+'+'+li[1]+'-'+li[2]+'-'+li[3]+'=7')

elif A-B+C+D==7:
  print(li[0]+'-'+li[1]+'+'+li[2]+'+'+li[3]+'=7')
  
elif A-B+C-D==7:
  print(li[0]+'-'+li[1]+'+'+li[2]+'-'+li[3]+'=7')
  
elif A-B-C+D==7:
  print(li[0]+'-'+li[1]+'-'+li[2]+'+'+li[3]+'=7')

elif A-B-C-D==7:
  print(li[0]+'-'+li[1]+'-'+li[2]+'-'+li[3]+'=7')



