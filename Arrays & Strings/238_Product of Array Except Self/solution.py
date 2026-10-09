class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        ptr = len(nums) - 1
        while ptr >= 1:
            answer[ptr-1] = answer[ptr] * nums[ptr]
            ptr = ptr - 1
        ptr = 1
        preMul = 1
        while ptr < len(nums):
            preMul = preMul * nums[ptr-1]
            answer[ptr] =  answer[ptr] * preMul
            ptr = ptr + 1
        return answer
        