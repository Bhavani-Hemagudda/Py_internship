# traversal

class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def inorder(root):
    if (root==None):
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)
def postorder(root):
    if (root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')
def preorder(root):
    if (root==None):
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(25)
root.left.left.left=Node(1)
print(inorder(root))
print(preorder(root))
print(postorder(root))


# level order

class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def levelorder(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(25)
root.left.left.left=Node(1)
print(levelorder(root))

# sum of nodes in a tree using recursion

class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def sum(root):
    if root is None:
        return 0
    return root.data + sum(root.left) + sum(root.right)
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(25)
root.left.left.left=Node(1)
print(sum(root))

# even node adding in tree

class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def even(root):
    if root is None:
        return 0
    current=root.data if root.data % 2 == 0 else 0
    return current +even(root.left) + even(root.right)
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(25)
root.left.left.left=Node(1)
print(even(root))

# height of the tree

class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return -1
    return 1+max(height(root.left),height(root.right))
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(25)
root.left.left.left=Node(1)
print(height(root))

# top view of the tree

class Node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def topview(root):
    print()
    q=[]
    d=dict()
    root.level=0
    q.append(root)
    while(len(q)!=0):
        root=q.pop(0)
        if root.level not in d:
            d[root.level]=root.data
        if root.left is not None:
            q.append(root.left)
            root.left.level=root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level=root.level+1
    for i in sorted(d):
        print(d[i],end=" ")


root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
root.right.left=Node(15)
root.right.right=Node(25)
root.left.left.left=Node(1)
print(topview(root))
