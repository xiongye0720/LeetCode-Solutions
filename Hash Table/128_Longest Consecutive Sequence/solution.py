class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visit = set()
        maxLen = 0
        for item in nums:
            if item not in visit:
                right = item
                while True:
                    if right not in nums:
                        break
                    visit.add(right)
                    right = right + 1
                left = item
                while True:
                    if left not in nums:
                        break
                    visit.add(left)
                    left = left - 1
                maxLen = max(maxLen,right-left-1)
        
        return maxLen
                