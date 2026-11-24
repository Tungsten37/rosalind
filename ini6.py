str=input()
ans={}
for word in str.split():
    if word in ans:
        ans[word]+=1
    else:
        ans[word]=1
for key, value in ans.items():
    print(key,value)