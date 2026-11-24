# 53. Maximum Subarray
# Given an integer array nums, 
# find the subarray with the largest sum, 
# and return its sum.


class Solution(object):
    def max(self,nums):
        n=len(nums)
        current_nums=0
        max_nums=nums[0]

        for i in range (n):
            current_nums+=nums[i]
            if current_nums>max_nums:
                max_nums=current_nums
            if current_nums<0:
                current_nums=0

        return max_nums

nums=list(map(int,input("Enter array :").split()))
obj=Solution()
result=obj.max(nums)
print(result)
