# maximum number in the list
l=list(map(int,input().split()))
for i in range(0,l):
    for j in range(i+1,l+1):
        if l[i]>l[j]:
            max=l[i]
print(max)

# num=int(input())
if num&1==0:
  print('even')
else:
    print('odd')

# swaping of two numbers without using temporary variable
a=10
b=9
a,b=b,a
print(a,b)

# find xor of 1 to n
def XoR(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
n=int(input("enter  a number"))
print(XoR(n))

# left to right xor
def XoR(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
l,r=map(int,input().split())
a=XoR(r)
b=XoR(l-1)
print(a^b)
