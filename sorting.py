#sorting an array
#insertion sort, acsending order
#break into sub problems, solving iteratively, stable alg., T: O(n^2)
from array import array
from re import L, S


def sortArray(self, arr: int) -> int:
    for i in range(1,len(arr)):
        j = i -1
        while (j>=0 and arr[j+1] < arr[j]):
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j -=1
    return arr

#merge sort, using recursion (two-branch) T: O(nlogn), M: O(n), and this is a stable alg.
#21 Merge K Sorted Linked Lists:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
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
        
    def mergeLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        #need something to start up the result list
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
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

#quicksort, designate a pivot, T: O(n^2) worst [O(nlogn)] best, generally not a stable alg

#215 Kth Largest Element in an Array worst case T: O(n^2), avg O(n), quick sort
#start at start and compare to pivot (last value)
def kLargest(self, nums: List[int], k:int) -> int:
    nums.sort()
    return nums[len(nums)-k]
def kLargest_real(self, nums: List[int], k:int) -> int:
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
#bucket sort T: O(n), and is not a stable alg at all...
#75 Sort Colors T: O(n) Bucket sort
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