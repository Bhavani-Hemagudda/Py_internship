# armstrong number
num=int(input("enter a number"))
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

# neon number
n=int(input("enetr a number:\n"))
sq=n*n
sum=0
while sq>0:
    d=sq%10
    sum=sum+d
    sq=sq//10
if n==sum:
    print("neon")
else:
    print("not neon")

# magic number
n=int(input("enter a number:"))
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

# composite number
n=int(input("enter a number:"))
if n<=1:
    print("not composite")
count=0
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        count+=1
if count>2:
    print("composite")
else:
    print("not composite")

# perfect number
n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not perfect number")

# strong number
n=int(input("enter a number:"))
org_num=n
fact=1
sum=0
while n>0:
    d=n%10
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
    fact=1
if org_num==sum:
    print("strong number")
else:
    print("not sstrong")

# spy number
n=int(input())
sum=0
mul=1
while n>0:
    d=n%10
    sum=sum+d
    mul=mul*d
    n=n//10
if sum==mul:
    print("spy number")
else:
    print("not spy number")

# merge two list
l1=
l2=list(map(int,input("enter a element:").split()))
l=l1+l2
l.sort()
print(l)

# swap first value and last value
l1=list(map(int,input("enter a elements:").split()))
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)

# print the list after deleting duplicates in it
l=list(map(int,input("enter a elements:").split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

# print the list elements which has occured odd number of times
l=list(map(int,input("enter a elements:").split()))
for i in set(l):
    count=0
    if l.count(i)%2!=0:
        print(i)

# sum of minimum three elements
l=list(map(int,input("enter a elements:").split()))
l.sort()
min_sum=sum(l[:3])
print(min_sum)

# police 
l=[1,-1,1,-1,-1,1,1,1]
p=0
uns=0
for i in l:
    if i==-1:
        if p>0:
            p-=1
        else:
            uns+=1
    else:
        p+=i
print(uns)
