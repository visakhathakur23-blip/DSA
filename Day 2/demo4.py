# 2520. Count the Digits That Divide a Number
 
class Solution(object):
    def divisible(self,num):
        temp=num
        ans=0
        while temp>0:
            r=temp%10
            if num%r==0:
                ans+=1
            temp//=10

            
        return ans
    


num=int(input("Enter your number: "))
obj=Solution()
result=obj.divisible(num)
print(result)