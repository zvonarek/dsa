import math
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
##########################################################################################
##########################################################################################
#LC 206 Reverse a Linked List
def reverseList(self, head:ListNode) -> ListNode: #T O(n), M O(1)
    prev, curr = None, head
    while (curr):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
def reverseList_recursive(self, head:ListNode) -> ListNode: #T O(n), M O(n)
    if not head:
        return None
    newHead = head
    if head.next:
        newHead = self.reverseList_recursive(head.next)
        head.next.next = head
    head.next = None
    return newHead
#LC 21 Merge Two Sorted Lists
def mergeLists(self, l1:ListNode, l2:ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1: tail.next = l1
    if l2: tail.next = l2
    return dummy.next
#LC 225 Implement Stack using Queues
class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x:int) -> None:
        self.q.append(x)
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
    def top(self) -> int:
        return self.q[-1]
    def empty(self) -> bool:
        return len(self.q) == 0
#LC 70 Climbing Stairs (DP)
def climbing(self, n: int) -> int:
    one, two = 1, 1
    for i in range(n-1):
        temp = one
        one += two
        two = temp
    return one
#LC 21 Merge K Sorted Linked Lists
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1) < len(lists) else None
                mergeLists.append(self.mergeList(l1,l2))
            lists = mergedLists
        return lists[0]
#LC 215 Kth Largest Element in an Array
def kLargest_cheap(self, nums: List[int], k:int) -> int:
    nums.sort()
    return nums[len(nums)-k]
def kLargest(self, nums: List[int], k:int) -> int:
    k = len(nums) - k
    def quickSelect(l,r):
        pivot, p = nums[r], l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p>k: return quickSelect(l,p-1)
        elif p >k: return quickSelect(p+1,r)
        else: return nums[p]
    return quickSelect(0,len(nums)-1)
#LC 75 Sort Colors
def sortColors(self, nums: List[int]) -> None:
    l, r = 0, len(nums) - 1
    i = 0
    def swap(i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    while i <= r:
        if nums[i] == 0:
            swap(l,i)
            l+=1
        elif nums[i] == 2:
            swap(i,r)
            r-=1
            i-=1
        i +=1
#LC 704 Binary Search
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l)//2) 
        if nums[m] > target: r = m - 1
        elif nums[m] < target: l = m + 1
        else: return m
    return -1
#LC 74 Search a 2D Matrix
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top +bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: break
        if not (top <= bot): return False
        row = (top+bot)//2
        l, r = 0, COLS-1
        while l <= r:
            m = (l+r) //2 
            if target > matrix[row][m]: l = m + 1
            elif target < matrix[row][0]: r = m - 1
            else: return True
        return False
#LC 374 Guess Number Higher or Lower
def guessNumber(self, n: int) -> int:
        l,r = 1,n
        while True:
            m = (l+r)//2
            res = guess(m) # guess is provided API
            if res > 0: l = m + 1
            if res < 0: r = m - 1
            else: return m
#LC 875 Koko Eating Bananas
def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res =r 
        while l<=r: 
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h: 
                res = min(res,k)
                r = k - 1
            else: l = k + 1
#LC 780 Search in a Binary Search Tree
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            # If end is reached or a node with a value of target is found found.
            return root # Return that node.
		# If target > current nodes value search in left side of node 
        # else search rightwards.
        if root.val > val: return self.searchBST(root.left,val)
        else: return self.searchBST(root.right,val) 
#LC 94 Binary Tree Inorder Traversal
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
#LC 230 Kth Smallest Element in a BST
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
#LC 105 Construct Binary Tree from Preorder and Inorder Traversal Arrays
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
#LC 112 Path Sum
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(node, curSum):
        if not node: return False
        curSum += node.val
        if not node.left and not node.right: return curSum == targetSum
        return (dfs(node.left, curSum) or dfs(node.right,curSum))
    return dfs(root,0)
#LC 78 Subsets 
def subSets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)
    dfs(0)
    return res
#LC 39 Combination Sum
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
#LC 199 Binary Tree Right Side View
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
#LC 103 Binary Tree Level Order Traversal
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