a,b,c=map(int,input().split())# for greatest of three numbers
if a>b and a>c:
    print("a")
elif b>c:
    print("b")
else:
    print("C")

age=int(input("enter your age:"))
if age > 18:
    print("you are allowed")
    elif age>75:
        print("risky")
    elif age>40:
        print("panic attack")
    else:
        print("dont scream")
else:
    print("not allowed")

#watermelon
w=int(input("enetre the weight "))
if w>=2 and w%2==0:
    x=w//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)
else:    
    print("no")

elephant
s=int(input("enetr the number of steps:"))
if s%5==0:
    print(s//5)#if divisible by five directly write
else:
    print(s//5+1)

#fizzbuzz
n=int(input("enter a number"))
if n%3==0 and n%5==0:
    print("fizzbuzz")
elif n%3==0:
    print("fizz")
elif n%5==0:
    print("buzz")
else:
    print("invalid number")

#fizzbuzz if number id divisible by 7 or and with 7 it should print buzz
n=int(input("eneter a number:\n"))
if n%7==0 or n%10==7:
    print("buzz")
else:
    print("not buzz")

#if two two numbers followed by are same 
n=int(input("enter a number:"))
if n%11==0:
    print("yes")
else:
    print("no")

# print even numbers between 50 to 100 including 100
for i in range(50,101,2):
    print(i)#for single line input use print(i,end=" ")

# another way
for i in range(50,101):
    if i%2==0:
        print(i,end=" ")

# to check number is prime or not
n=int(input("enter a number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print(" prime")

# the prime numbers between 5 and 15
def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
l=int(input())
r=int(input())
c=0
for i in range(l,r+1):
    if isprime(i):
        c+=1
print(c)

# for the sum of numbers:
n=int(input("enter numbrt:"))
sum=0
while n!=0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)
n=int(input("enter number"))#count of digit
count=0
while n!=0:
    count+=1
    n=n//10
print(count)

# reverse the number
n=int(input("enter numbrt:"))
sum=0
while n!=0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)

# for limak and bob
limak,bob=map(int,input().split())
year=0
while limak<=bob:
    limak*=3
    bob*=2
    year+=1
print(year)

#sum of digits is prime or not  that is googly number
n=int(input())
sum=0
while n!=0:
   d=n%10
   sum=sum+d
   n=n//10
flag=0
for i in range(2,sum):
  if sum%i==0:
      flag+=1
  if flag==0:
      print("googly")
  else:
       print("not googly")
