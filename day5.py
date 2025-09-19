# count of alphabets and digits in a string
s=input()
ca=0
cd=0
for char in s:
    if char.isalpha():
        ca+=1
    if char.isdigit():
        cd+=1
print(ca,cd)

# count of vowels and consonants
s=input()
cv=0
cc=0
v='a','e','i','o','u'
for  char in s:
    if char in v:
        cv+=1
    if char not in v:
        cc+=1
print(cv,cc)

# replace space with hyphen
s=input()
s1=""
for char in s:
    if char.isspace():
        s1+='-'
    else:
        s1+=char
print(s1)

# capitalize first letter in each word
s=input()
s=s.title()
print(s)

# capitalize first letter without using title
s=input()
w=s.split()
res=""
for  word in w:
    cap=word[0].upper()+word[1:]
    res=res+" "+cap
print(res)

# revers a string without using slicing
s=input()
s1=" "
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
print(s1)

# length of longest word in length
s=input()
l=s.split()
length=0
lword=''
for word in l:
    if len(word)>length:
        length=len(word)
        lword=word
print(length)
print(lword)


# check whether string is palindrome 
s=input()
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# remove duplictes in a string
s=input()
s1=" "
for i in s:
    if i not in s1:
        s1+=i
print(s1)

# most frequent character in word
s=input()
freq={}
for i in s:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
m=max(freq.values())
for i in freq:
    if freq[i]==m:
        print(i)

# password validator
password=input()
lc,uc,lwc,dc,spc,cc=1,1,1,1,1,0
fc=0
spc_count=0
l=len(password)
for i in range(len(password)):
    if password[i].isupper():
        up=0
    if password[i].islower():
        lc=0
    if password[i].isdigit():
        dc=0
    if i+1<l and password[i]==password[i+1]:
        cc=1
    if l >= 6 and l <= 22:
        lwc=0
    if password[i] in "!@#$%^&*":
        spc_count+=1
    if spc_count>=2:
        sp=0
fc=uc+lc+dc+spc+cc+lc+lwc
print(fc)



# palindrome 
s=input()
i,j=0,len(s)-1
while i<=j:
    if s[i]!=s[j]:
        print("False")
        break
    i+=1
    j-=1
else:
    print("True")


    

      




