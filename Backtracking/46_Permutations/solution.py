class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(ans,lvl,tar,nums):
            temNum = nums[lvl-1]
            nums[lvl-1] = nums[tar]
            nums[tar] = temNum

            if lvl == maxLvl:
                temAns = []
                for item in nums:
                    temAns.append(item)
                ans.append(temAns)
                nums[tar] = nums[lvl-1]
                nums[lvl-1] = temNum
                return
            
            for i in range(lvl,len(nums)):
                DFS(ans,lvl+1,i,nums)
            
            nums[tar] = nums[lvl-1]
            nums[lvl-1] = temNum

        
        maxLvl = len(nums)
        ans = []
        for i in range(len(nums)):
            DFS(ans,1,i,nums)

        return ans
        