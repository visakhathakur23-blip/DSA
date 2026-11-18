##Recursion


def num(i,n):
    if i>n:
        return
    print(i,end=" ")
    num(i+1,n)
num(1,5)


#factorial
def fact(n):
    if n==0:
        return 1
    return n*fact (n-1)

print(fact(5))


def fun(n):
    if n==0:
        return

    print(n,end=" ")
    fun(n-1)

fun(3)



def fun(n):
    if n==0:
        return
    
    fun(n-1)
    print(n,end=" ")
    

fun(6)

