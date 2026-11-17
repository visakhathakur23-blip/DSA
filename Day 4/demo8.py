# ### liner time complexity 0(n)
n=10
for i in range (n) :
    print(i,end =" ")


for i in range (n*10) :
    print(i,end =" ")

m=90
for i in range (n+m) :
    print(i,end =" ")




### Constant time complexity 0(1)

for i in range (10) :
    print(i,end =" ")


# ### QUADRATIC time complexity 0(n^2 )

for i in range (n**2) :
    print(i,end =" ")


### Logarithmic time complexity 0(log(n) )

n=100

while n>0:
    print(n,end=" ")
    n//=2


i=1
n=100

while i<=n:
    print(i,end=" ")
    i*=2