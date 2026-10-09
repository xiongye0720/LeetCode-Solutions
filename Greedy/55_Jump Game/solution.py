class Solution:
    def canJump(self, nums: List[int]) -> bool:
        Left = 0
        while True:
            if Left == len(nums)-1:
                return True
            else:
                if nums[Left] == 0:
                    return False
                elif Left+nums[Left] > len(nums)-1:
                    return True
                else:
                    Tem = (Left+nums[Left],Left+nums[Left]+nums[Left+nums[Left]])
                    TemEnd = Tem[0]
                    Left = Left + 1
                    while Left < TemEnd:
                        if Left+nums[Left] > Tem[1]:
                            Tem = (Left,Left+nums[Left])
                        Left = Left + 1
                    Left = Tem[0]
