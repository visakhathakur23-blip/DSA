# 509.The Fibonacci numbers, commonly denoted F(n) form a sequence,
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
# starting from 0 and 1. That is,F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


class solution(object):
    def fibno(self,n):
        if n==0 or n==1:
            return n
        return self.fibno(n-1)+self.fibno(n-2)

n=int(input("enter your number: "))
obj=solution()
result=obj.fibno(n)
print(result)
