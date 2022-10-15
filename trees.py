#binary trees, can remove/insert in O(log n) so long as it is roughly balanced
#BST: recursive, if balanced tree: heights of sub trees ~ each other
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def search(root, target): #T: O(log n)
    if not root: return False
    if target > root.val: return search(root.right, target)
    elif target < root.val: return search(root.left, target)
    else: return True
# 700 Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val: # If end is reached or a node with a value of target is found found.
            return root # Return that node.
		# If target > current nodes value search in left side of node else search rightwards.
        return self.searchBST(root.left,val) if root.val > val else self.searchBST(root.right,val) 

def insert(root, val): #T: O(log n)
    if not root: return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right,val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

#removing a node: either the node has 0 or 1 child, or has 2 children
#simple case
def remove(root, val): #T: O(log n) better than sorted arrays
    if not root: return None
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left: return root.right
        elif not root.right: return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

#Depth-First-Search (DFS) start at a node then go as far deep as you can first
#traversing a BST T: O(n)
#sorting a BST: O(log n)
def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
def preorder(root): #visit before printing subtrees
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
def postorder(root): #traverse all values then print rootnode
    if not root: return 
    postorder(root.left)
    postorder(root.right)
    print(root.val)
def reverseorder(root):
    if not root: return
    inorder(root.right)
    print(root.val)
    inorder(root.left)
# 94 Binary Tree Inorder Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
#230 Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
#105 Contruct Binary Tree from Preorder and Inorder Travesal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root