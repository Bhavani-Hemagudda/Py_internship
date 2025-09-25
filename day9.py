# bubble sort:

a=[3,7,6,5,9,1,2,4]
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


# selection sort:

a=[4,1,2,5,6,3]
n=len(a)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if a[j]<na[min]:
            min=j
    a[i],a[min]=a[min],a[i]
print(a)


# insertion sort:

a=[7,5,4,8,2,1,3]
n=len(a)
for i in range(1,n):
    v=a[i]
    j=i-1
    while j>=0 and a[j]>v:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=v
print(a)


# quick sort:

def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left=[x for x in a[1:] if x<=pivot]
    right=[x for x in a[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
a=[5,3,8,4,2,7,1,10]
print(quick_sort(a))


# merge sort:

def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
a=[5,2,9,1,6,3]
print(merge_sort(a))



# linked list:

class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class SLL:
    def _init_(self):
        self.head=None
    def Insert_at_begin(self,data):
        print()
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
    def Insert_at_end(self,data):
        print()
        new1=Node(data)
        if self.head is None:
            self.head=new1
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new1
    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
    def Insert_at_specific(self,data,pos):
        print()
        new2=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new2.next=temp.next
        temp.next=new2
    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
    def deletion_at_begining(self):
        print()
        temp=self.head
        self.head=temp.next
        temp.next=None
    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
    def deletion_at_end(self):
        print()
        prev=self.head
        temp=self.head.next
        while temp.next!=None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
    def deletion_at_particular(self,pos):
        print()
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
n1=Node(5)
sll=SLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.nexxt=n3
sll.Traversal()
sll.Insert_at_begin(2)
sll.Traversal()
sll.Insert_at_end(20)
sll.Traversal()
sll.Insert_at_specific(8,3)
sll.Traversal()
sll.deletion_at_begining()
sll.Traversal()
sll.deletion_at_end()
sll.Traversal()
sll.deletion_at_particular(3)
sll.Traversal()



# sum of all nodes in the linked list:

class Node:
    def _init(self, data):   # fixed __init
        self.data = data
        self.next = None

class SLL:
    def _init(self):         # fixed __init
        self.head = None

    def Insert_at_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def Traversal(self):
        if self.head is None:
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    def Sum_all_nodes(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.data
            temp = temp.next
        return total

    def Sum_even_nodes(self):
        total = 0
        temp = self.head
        while temp:
            if temp.data % 2 == 0:   # only even numbers
                total += temp.data
            temp = temp.next
        return total


# Example usage
s = SLL()
s.Insert_at_begin(5)
s.Insert_at_begin(8)
s.Insert_at_begin(3)
s.Insert_at_begin(10)

s.Traversal()

print("Sum of all nodes:", s.Sum_all_nodes())
print("Sum of even nodes:", s.Sum_even_nodes())



# middle of the linked list:

class Solution:
    def middleNode(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
