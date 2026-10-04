#input we have get
s=input("")
#it store current substring without duplicate
ans=""
max_len=0
for ch in s:
    #remove the duplicate
    if ch in ans:
        ans=ans[ans.index(ch)+1:]
    ans +=ch
    #update max length
    if len(ans)>max_len:
        max_len=len(ans)
print(max_len)
