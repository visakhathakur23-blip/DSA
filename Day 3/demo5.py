# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution(object):
    def palindrome(self,x):
        temp=x
        rev=0

        while temp>0:
            r=temp%10
            temp//=10
            rev=rev*10+r

        return rev==x

x=int(input("Enter your number:"))
obj=Solution()
result=obj.palindrome(x)
print(result)