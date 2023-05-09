if(4%2==0):
    print("4 is even")
else:
    print("4 is odd")

a = int(input("Enter a number"))
if(a%2==0):
    print(a," is even")
else:
    print(a," is odd")

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
if(a>b):
    if(a>c):
        print(a,"is greater")
    else:
        print(b,"is greater")
else:
    if(b>c):
        print(b,"is greater")
    else:
        print(c,"is greater")

def GCD(m,n):
    if m<n:
        (m,n) = (n,m)
    while m%n != 0:
        (m,n) = (n,m%n)
    
    return(n)
print(m," ",n)
m = int(input("enter m:"))
n = int(input("enter n:"))
print(GCD(m,n))

for i in range (1,10):
    print("In a loop")

a = 30/0
print(a)

a = [23,"I"]
print(a[3])

prin(54)

import mathe

li = {1: 1, 2: 4, 3: 9}
print(li[4])

li = {1:1}
print(li[1])



