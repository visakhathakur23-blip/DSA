# 905.Sort Array By Parity
#  Given an integer array nums,
#  move all the even integers at the
#  beginning of the array followed by
#  all the odd integers.

# Return any array that satisfies this condition.


class Solution(object):
    def parity(self,nums):

        n=len(nums)

        start=0

        for i in range (n):
            if nums[i]%2==0:
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1

        return nums

nums=list(map(int,input("Enter array to sort: ").split()))
nums.sort
obj=Solution()
result=obj.parity(nums)
print (result)