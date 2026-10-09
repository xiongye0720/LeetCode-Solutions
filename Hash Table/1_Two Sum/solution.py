class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map previously visited values to their indices.
        numsDict = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in numsDict:
                return [numsDict[rem],i]
            else:
                # Insert after checking to avoid using the same element twice.
                numsDict[nums[i]] = i


        