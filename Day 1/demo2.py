# 1523. Count Odd Numbers in an Interval Range

class solution(object):
    def countoddno(self,low,high):
        return (high+1)//2-(low//2)

low=int(input("Enter the low no:"))
high=int(input("Enter the high no:"))
obj=solution()
result=obj.countoddno(low,high)
print(result)

    