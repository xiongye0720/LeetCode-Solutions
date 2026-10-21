class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        length = len(nums)

        sumDict = {}
        for i in range(length):
            temSum = 0
            for j in range(i,min(i+2,length)):
                temSum = temSum + nums[j]
                # Only record subarrays of length two.
                if j-i != 1:
                    continue
                # Group index pairs by their subarray sum.
                if temSum in sumDict:
                    sumDict[temSum].append((i,j))
                else:
                    sumDict[temSum] = [(i,j)]

        maxLen = 0
        for key in sumDict:
            maxLen = max(maxLen,len(sumDict[key]))

        # A repeated sum means two distinct subarrays have equal sums.
        return maxLen >= 2