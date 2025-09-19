# checking power of 2
n=int(input("enter number"))
while n:
    if n==1:
        print("yes")
        break
    if n%2!=0:
        print("no")
        break
    n=n//2

# to delete element in tuple
t=(1,2,3,4,5,6,7,8)
t=t[:5]+t[6:]
print(t)

# palindrome 
x=int(input()) 
if x<0:
    print("False")
rev=0
original=x
while(x):
    rev=rev*10+x%10
    x//=10
if(original==rev):
    print("palindrome")
else:
    print("not palindrome")



# python program to chech if key exis in dictionary
student_marks={'sita':95,
               'akash':80,
               'anvesh':56,
               'honey':41,
               'mallesh':15,
               'arjun':54,
               'mani':29}
student_grades={}
for s in student_marks:
    marks=student_marks[s]
    if marks >90:
        student_grades[s]='A+'
    elif marks>80:
        student_grades[s]='A'
    elif marks>70:
        student_grades[s]='B+'
    elif marks>60:
        student_grades[s]='B'
    elif marks>50:
        student_grades[s]='c+'
    elif marks>40:
        student_grades[s]='c'
    else:
        student_grades[s]='F'
print(student_grades)




