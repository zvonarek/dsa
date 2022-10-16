#BST implemented sets/maps (dict)
#simiar to sets but keys are mapped to val and keys can access values
#hash maps cannot contain duplicates, same with TreeMaps
#TreeMap HashMap    Operation
#O(logn) O(1)       Insert
#O(logn) O(1)       Remove
#O(logn) O(1)       Search
#O(n)    O(nlogn)   InOrder
#Hashmaps don't maintain any type of ordering

names = [ "bebz", "brandon", "kerry", "kevin", "mindy" ]
countMap = {}
for name in names:
    if name not in countMap: countMap[name] = 1
    else: countMap[name] += 1

#LC 217 Contains Duplicate
def containsDuplicate(self, nums: list[int]) -> bool:
    hashset = set()
    for n in nums: 
        if n in hashset: return True
        hashset.add(n)
    return False
# LC 1 Two Sum
def twoSum(self, nums: list[int], target: int) -> list[int]:
    prevMap = {} # val : index
    for i,n in enumerate(nums):
        diff = target - n 
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return
#LC 146 LRU Cache
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity:int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.orev = nxt, prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key:int, value:int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache(lru.key)
#implementation of hash map
#COME BACK TO THIS (as of 16 Oct. 23)
