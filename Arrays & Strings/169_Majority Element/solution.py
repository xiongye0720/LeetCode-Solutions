class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        col = [None,0]
        for item in nums:
            if col[0] is None:
                col = [item,1]
            else:
                if item == col[0]:
                    col[1] = col[1] + 1
                else:
                    col[1] = col[1] - 1
                    if col[1] == 0:
                        col[0] = None
        return col[0]