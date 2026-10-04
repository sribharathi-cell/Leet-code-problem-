#input
nums = list(map(int, input().split()))
#array to set for easy check
num_set=set(nums)
longest=0
for num in num_set:
    if num-1 not in num_set:
        length=1
        while num+length in num_set:
            length +=1
        longest=max(longest,length)
print ("LENGTH:",longest)
