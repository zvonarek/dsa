#binary search, T: O(log n)
#return index of target
#704 Binary Search 
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l)//2) # avoid overflow
        if nums[m] > target: r = m - 1
        elif nums[m] < target: l = m + 1
        else: return m
    return -1
#74 Search a 2D Matix T: O(mlogn), and we can do better...
class Solution:
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

#Search range T: O(log n), n is the range of values we are searching

#374 Guess Number Higher or Lower, T: O(log n), M: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n
        while True:
            m = (l+r)//2
            res = guess(m) # guess is provided API
            if res > 0: l = m + 1
            if res < 0: r = m - 1
            else: return m

#875 Koko Eating Bananas
class Solution:
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