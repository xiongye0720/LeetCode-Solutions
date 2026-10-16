class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxValue(nums,start,end):
            if end-start+1 <= 2:
                return max(nums[start:end+1])
            else:
                ops = deque()
                ops.append(nums[start])
                ops.append(nums[start+1])
                temVal = 0
                for i in range(2,end-start+1):
                    temVal = max(temVal,ops.popleft())
                    ops.append(temVal+nums[start+i])
                return max(ops)

        if len(nums) <= 3:
            return max(nums)
        else:
            dp = []
            for i in range(3):
                temVal = maxValue(nums,i+1,len(nums)-3+i)
                dp.append(temVal+nums[(len(nums)-1+i)%len(nums)])

            return max(dp)