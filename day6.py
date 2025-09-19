# length of longest palindrome

s="abba"
m=0
for c in range(len(s)):
    l,r=c,c
    while l>=0 and r<len(s) and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
    l,r=c,c+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
print(m)

# squaring using lambda
s=lambda n:n*n
n=int(input())
res=s(n)
print(res)

# using lambda addition 
f=lambda a,b:a+b
n=int(input())
m=int(input())
result = f(n,m)
print(result)

# even number without using lambda function
def even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(even,nums))
print(evens)

# using lambda function for even
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)

# using map multiply for even  number
def update(n):
    return n*2
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(update,evens))
print(doubles)


# adding the doubled number of even using lambda
from functools import reduce
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
num=reduce(lambda a,b:a+b,doubles)
print(doubles)
print(num)


# armstrong number
def armstrong(num):
    temp1=num
    temp2=num
    c=0
    while temp1>0:
        c+=1
        temp1=temp1//10
    sum=0
    while temp2>0:
        d=temp2%10
        sum=sum+d**c
        temp2=temp2//10
    if sum==num:
        print("armstrong")
    else:
        print("not armstrong")
armstrong(153)

# magic number
def magic_number(n):
    while n>9:
        sum=0
        while n>0:
            d=n%10
            sum=sum+d
            n//=10
        n=sum
    if n==1:
        print("magic number")
    else:
        print("not magic number")
magic_number(12)

# perfect number
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if n==sum:
        print("perfect number")
    else:
        print("not perfect number")
perfect_number(14)


# print 5 4 3 2 1 2 3 4 5 if i/p is 5 
def nums(n):
    if n==0:
        return
    if n==1:
        print(n,end="")
        return 
    print(n,end=" ")
    nums(n-1)  
    print(n,end=" ")
n=int(input())
nums(n)

# factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1)*n
n=int(input())
print(factorial(n))


# palindrome using recursion
def is_palindrome(n,rev=0,temp=None):
    if temp is None:
        temp=n
    if n==0:
        return temp==rev
    return is_palindrome(n//10,rev*10+n%10,temp)
num=int(input())
print(is_palindrome(num))


# reverse an integer using recursion
def reverse_number(n,rev=0):
    if n==0:
        return rev
    return reverse_number(n//10,rev*10+n%10)
num=int(input("enter numbrt:"))
print(reverse_number(num))


# perfect square
def is_square(n, i=1):
    if i * i == n:
        return True
    if i * i > n:
        return False
    return is_square(n, i + 1)
num = int(input("Enter a number: "))
print("Perfect square" if is_square(num) else "Not a perfect square")


# power of 2 
def power_of_2(x):
    if x == 1:
        return True
    if x == 0 or x % 2 != 0:
        return False
    return power_of_2(x // 2)

n = int(input("Enter number: "))
print(power_of_2(n))


# reduce number by 1 and count minimum  steps to reduce a number geeks  for geeks
def countways(n):
    if (n == 1):
        return 0
    elif (n % 2 == 0):
        return 1 + countways(n / 2)
    else:
        return 1 + min(countways(n - 1), 
                    countways(n + 1))
n = 7
print(countways(n))









    




