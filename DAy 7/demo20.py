# 1480 Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


class Solution(object):
    def runningsum(self,nums):
        n=len(nums)
        
        ans=[]
        ans.append(nums[0])

        for i in range(1,n):
            x=ans[i-1]+nums[i]
            ans.append(x)

        return ans

nums=list(map(int,input("Enter number : ").split()))
obj=Solution()
result=obj.runningsum(nums)
print(result)
