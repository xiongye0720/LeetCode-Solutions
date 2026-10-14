class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            maxVal = 0
            ops = deque()
            ops.append(nums[0])
            ops.append(nums[1])

            for i in range(2,len(nums)):
                maxVal = max(maxVal,ops.popleft())
                ops.append(maxVal+nums[i])

            return max(ops)