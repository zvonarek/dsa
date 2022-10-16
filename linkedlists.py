#ll: value and next (pointer)
#traversal O(n)
#adding element O(n)
# adding node to end:
    # tail.next = ListNode4
    # tail = tail.next
#removing node O(n)
    #head.next = head.next.next

#206 Reverse a linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

#21 Merge Two Sorted Lists
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

#doubly ll:
#insert/remove and end or middle O(1), access i-th element O(n)
#contrasted to arrays: insert/remove end and accessing i-th element O(1), insert/remove
#at the middle is O(n)