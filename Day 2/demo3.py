# 1365. How Many Numbers Are Smaller Than the Current Number



class Solution (object):
    def smallerno(self,nums):
        ans=[]
        for i in nums:
            c=0
            for j in nums:
                if j<i:
                    c+=1
            ans.append(c)
        return ans 




nums=list(map(int,input( "enter the number:").split()))
obj=Solution()
result=obj.smallerno(nums)
print(result)


    
