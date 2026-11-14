# 1281. Subtract the Product and Sum of Digits of an Integer

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

class Solution(object):
    def difference(self,n):
        temp=n
        add=0
        product=1

        while temp>0:
            r=temp%10
            temp//=10
            add+=r
            product*=r

            
        return product-add
    


n=int(input("Enter your number: "))
obj=Solution()
result=obj.difference(n)
print(result)