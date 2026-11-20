# 231 Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

class solution(object):
    def ispoweroftwo(self,n):
        while n%2==0:
            n//=2
            
        if n==1:
            return True
        else:
            return False

n=int(input("enter your number: "))
obj=solution()
result=obj.ispoweroftwo(n)
print(result)



class solution(object):

 def ispoweroftwo(self,n):
  if n<=0:
   return False
  if n==1:
   return True
  if n%2!=0:
   return False 

  return self.ispoweroftwo(n//2)


n=int(input("enter your number: "))
obj=solution()
result=obj.ispoweroftwo(n)
print(result)


