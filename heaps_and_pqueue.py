#heaps/priority queue (ordered by p-value)
#binary heap is min or max depending on pqueue looking for min or max
#heaps are Binary trees, considered complete: every level is full, except last one
#the order value: recursively, all vals in left are less than root, vice a versa
#these are just implemented using arrays and dont care about the 0th ind place root at 1
#left child = 2*i, right child = 2*i + 1 and parent = i//2, only true because complete T
#for pushing we need to make sure both props are satisfied
from re import L


class Heap: #T: O(log n) since the tree is balanced
    def __init__(self):
        self.heap = [0]
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        #percolate up while order is not satisfied
        while self.heap[i] < self.heap[i//2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i = i//2
#last node, move to root, percolate down
def pop(self): #T: O(log n) since balanced tree
    if len(self.heap) == 1: return None
    if len(self.heap) == 2: return self.heap.pop()
    res = self.heap[1]
    self.heap[1] = self.heap.pop()
    i = 1
    while 2*i < len(self.heap):
        if (2*i + 1 < len(self.heap) and 
        self.heap[2*i + 1] < self.heap[2*i] and 
        self.heap[i] > self.heap[2*i +1]):
            tmp = self.heap[i]
            self.heap[1] = self.heap[2*i + 1]
            self.heap[2*i + 1] = tmp
            i = 2*i + 1
        elif self.heap[i] > self.heap[2*i]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[2*i]
            self.heap[2*i] = tmp
            i = 2*i
        else: break
    return res

#LC 703 Kth Largest Element in a Stream
#min heap of size k, pop the min val and grab the kth min val
class KthLargest:
    def __init__(self, k:int, nums: list[int]):
        self.minHeap, self.k, nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val:int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k: heapq.heappop(minHeap)
        return self.minHeap[0]

#LC 973 K Closest Points to Origin
def kClosest(self, points: list[list[int]], k:int) -> list[list[int]]:
    minHeap = []
    for x,y in points:
        dist = (x**2) + (y**2)
        minHeap.append([dist,x,y])

    heapq.heapify(minHeap)
    res = []
    while k >0:
        dist,x,y = heapq.heappop(minHeap)
        res.append([x,y])
        k -=1
    return res

#LC 1046 Last Stone Weight
def lastStone(self, stones:list[int] ) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first: heapq.heappush(stones, first-second)
    stones.append(0)
    return abs(stones[0])