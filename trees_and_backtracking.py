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

#Breadth First Search (BFS), T: O(n), M:
from collections import deque
from operator import le
def bfs(root):
    queue= deque()

    if root: queue.append(root)
    level = 0
    while len(queue) >0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        level +=1
#102 Binary Tree Level Order Traversal, T: O(n)
class Solution:
    from collections import deque
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                if level:
                    res.append(level)
        return res
#199 Binary Tree Right Side View
#use a queue, add root node and add rightmost to res array
#add right/left child and then remove the right value after adding its children
#add left to the res
def rightSideView(self, root: TreeNode) -> List[int]:
    res = []
    q = collections.queue([root])
    while q:
        rightSide = None
        qLen = len(q)

        for i in range(qLen):
            node = q.popleft()
            if node: 
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide: res.append(rightSide.val)
    return res

#Sets/Maps, implemented with BFS, like Queues are made w LL, and Stacks are made w/ arrays
from sortedcontainers import SortedDict
treeMap = SortedDict({'c':1, 'a':1, 'b':2})

#backtracking, T: O(n) this is a brute force alg
def canReachLevel(root):
    if not root or root.val == 0: return False
    if not root.left and not root.right: return True
    if canReachLevel(root.left): return True
    if canReachLevel(root.right): return True
    return False
#determine if a path exists from the root of the tree to a leaf node, cannot conatin zeros
def leafPath(root, path):
    if not root and root.val == 0: return False
    path.append(root.val)
    if not root.left and not root.right: return True
    if leafPath(root.left, path): return True
    if leafPath(root.right, path): return True
    path.pop()
    return False
#112 Path Sum
#need to go through all the paths and see if it ends up totalling target val
#inorder DFS problem while maintaining sum T: O(n), M: O(n), O(log n) if balanched
def Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node: return False
            curSum += node.val
            if not node.left and not node.right: return curSum == targetSum
            return (dfs(node.left, curSum) or dfs(node.right,curSum))
        return dfs(root,0)
#78 Subsets 
def subSets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        #include nums[i]
        subset.append(nums[i])
        dfs(i+1) #left branch
        #not to include nums[i]
        subset.pop()
        dfs(i+1)
    dfs(0)
    return res
#39 Combination Sum, T: O(2^t)
def combinationSum(self, candidates: List[int], target:int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target: 
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target: return
        candidates[i]
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i+1,cur,total)
    dfs(0,[],0)
    return res
