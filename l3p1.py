# LAB 3


## power using for loop

def power(n,p):
    pw = 1
    for i in range(p):
        pw = pw * n
    return pw
print(power(5,3))

## LINEAR SEARCH
### WITHOUT FUNCTION

arr = [1,2,3,4,5]
num = 7
count = 0
for i in range(0,5):
    if(arr[i] == num):
        print(num, "present in ",i+1,"th position")
        count = count+1
if(count<1):
    print("not found")

### WITH FUNCTION

def search(arr,num):
    cnt = 0
    for i in range(0,len(arr)):
        if(arr[i]==num):
            cnt = cnt+1
            print("Element found in ",i,"th position")
    if(cnt == 0):
        print("Element not found")
        
arr = [1,2,3,4,5]
search(arr,0)        

### MAXIMUM OF LIST OF NUMBER


def largest(arr,n):
    max = 0
    for i in range(n):
        if(max < arr[i]):
            max = arr[i]
        
    return max
    
    

    
arr = []
n = int(input("enter no of elements:"))
for i in range(n):
    e = int(input())
    arr.append(e)
print("largest number in the array is",largest(arr,n))

import numpy as np

a = [1,2,3]
type(a)
print(a)

arr = np.array(a)
type(arr)
print(arr)

### ROTATE THE LIST

def listrot(arr,n):
    first = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = first

arr = []
n = int(input("enter no of elements:"))
for i in range(n):
    e = int(input())
    arr.append(e)
print(arr)
for i in range(3):
    listrot(arr,n)
print("After 3 rotation")
print(arr)
