# security key

 n=int(input())
 s=str(n)
 l=[]
 for i in s:
     if i not in l:
         l.append(i)
 a=len(s)
 b=len(l)
 c=a-b
 print(c)




# encode means which which number is reapeated greater number of times in array o/p=5

 n=22455564634
 m=3
 s=str(n)
 d={}
 for i in s:
     if i not in d:
         d[i]=1
     else:
         d[i]+=1
 res=0
 for i in d:
     if d[i]==m:
         res=i
 print(res)


# adjacent element sum of their difference o/p=9

 s=[3,4,5,6,8,4]
 sum=0
 for i in range(len(s)-1):
     sum+=abs(s[i]-s[i+1])
    
 print(sum)

# odd even online game

 arr=[1,4,2,6,7,8,2,9,10,11]
 l=[]
 for i in arr:
     if i%2==0:
         l.append(i)
 for i in arr:
     if i%2!=0:
         l.append(i)
 print(l)

# secretmessage

 n=input()
 for i in range(len(n)):
     if i is not  alnum():
         print(i)


#perfect square numbers

arr = [1, 2, 4, 7, 9, 16, 20, 25, 30]
count = 0

for num in arr:
    root = int(num ** 0.5)
    if root * root == num:
        count += 1

print("Perfect square count:", count)



