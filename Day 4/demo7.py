# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

class Solution(object):
    def candies(self,candies,extracandies):
        maxcandies=max(candies)

        ans=[]

        for i in candies:
            if(i+extracandies)>=maxcandies:
                print("True")
            else:
                print("False")


candies=list(map(int(input("Enter the candies:").split())))
extracandies=int(input("Enter the extracandies:"))
obj=Solution()
result=obj.candies(candies,extracandies)
print(result)
