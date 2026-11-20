# 1137 The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.


class solution(object):
    def tri(self,n):
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        return self.tri(n-1)+self.tri(n-2)+self.tri(n-3)

n=int(input("Enter your no: "))
obj=solution()
result=obj.tri(n)
print(result)