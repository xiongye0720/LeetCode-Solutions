class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Store the most recent index of each value.
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] in numsDict:
                # The most recent occurrence gives the smallest index gap.
                if i-numsDict[nums[i]] <= k:
                    return True
                else:
                    numsDict[nums[i]] = i
            else:
                numsDict[nums[i]] = i
        
        return False
            
