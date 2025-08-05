from collections import deque
class TreeNode:
    def __init__(self,val,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.val)
    

A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)

A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
print(A)

def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)

def pre_order_iterative(node):
    stk=[node]

    while stk:
        node=stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
pre_order_iterative(A)

def level_order(node):
    q=deque()
    q.append(node)
    
    while q:
        node=q.popleft()
        print(node)

        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)

print("#############")
def search(node,target):
    #print(node)
    if not node:
        return False
    
    if node.val==target:
        return True
    
    return search(node.left,target) or search(node.right,target)

print(search(A,6))


A2=TreeNode(5)
B2=TreeNode(3)
C2=TreeNode(8)
D2=TreeNode(2)
E2=TreeNode(4)
F2=TreeNode(7)

A2.left=B2
A2.right=C2
B2.left=D2
B2.right=E2
C2.left=F2

print(A2)


in_order(A)

print("*******")
def search_bst(node,target):
    if not node:
        return False
    if node.val==target:
        return True
    
    if target<node.val:
        return search_bst(node.left,target)
    else:
        return search_bst(node.right,target)
    
search_bst(A2,4)

def deleteBST(self,root,key):
    if not root:
        return
    if root.val == key:
        if not root.left and not root.right:
            return None
        if not root.left and root.right:
            return root.right
        if not root.right and root.left:
            return root.left
        
        ptr=root.right
        while ptr.left:
            ptr=ptr.left

        root.val = ptr.val
        root.right = self.deleteBST(self,root.right,root.val)

    elif key < root.val:
        root.left = self.deleteBST(self,root.left,root.val)
    else:
        root.right = self.deleteBST(self,root.right,root.val)
    return root
