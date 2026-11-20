#326 Given an integer n, return true if it is a power of three. Otherwise, return false.
#An integer n is a power of three, if there exists an integer x such that n == 3x.

# class Solution(object):
#     def isPowerofThree(self,n):
#         if n<=0:
#             return False
#         if n==1:
#             return True
#         if n%3!=0:
#             return False
#         return self.isPowerofThree(n//3)

# n=int(input("Enter no: "))
# obj=Solution()
# result=obj.isPowerofThree(n)
# print(result)



class Solution(object):
    def isPowerofThree(self,n):

        while n%3==0:
            n//3

        if n==1:
            return True
        else:
            return False

n=int(input("Enter no: "))
obj=Solution()
result=obj.isPowerofThree(n)
print(result)
