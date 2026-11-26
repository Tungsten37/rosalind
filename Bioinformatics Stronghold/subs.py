s=input().strip()
t=input().strip()
sn=len(s)
tn=len(t)
ans=[]
for i in range(sn-tn+1):
    if (s[i:i+tn]==t):
        ans.append(i+1)
print(*ans)