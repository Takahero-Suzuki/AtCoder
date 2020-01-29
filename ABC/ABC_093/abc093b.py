A,B,K=map(int,input().split())

small=[n for n in range(A,min(A+K,B+1))]

large=[n for n in range(max(A,B-K+1),B+1)]

ans_set=set(small+large)
ans=list(ans_set)
ans.sort()
ans_str=list(map(str,ans))

print(' '.join(ans_str))

# 別解
A,B,K=map(int,input().split())

small=[n for n in range(A,min(A+K,B+1))]
# rangeの最小値をAまたはB-K+1とすると通らないので若干厳密にやらないと間違える
large=[n for n in range(max(A+K,B-K+1),B+1)]

ans=small+large
ans.sort()
ans_str=list(map(str,ans))

print(' '.join(ans_str))
