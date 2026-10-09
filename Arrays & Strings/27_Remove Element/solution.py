class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) > 0:
            # Count the elements to keep.
            Count = 0
            for item in nums:
                if item != val:
                    Count = Count + 1
            LeftW = 0
            RightW = len(nums) - 1
            # Fill the first Count positions using valid elements from the suffix.
            while LeftW<Count and RightW>=Count:
                if nums[LeftW] == val:
                    while RightW >= Count:
                        if nums[RightW] != val:
                            nums[LeftW] = nums[RightW]
                            LeftW = LeftW + 1
                            RightW = RightW - 1
                            break
                        # Skip suffix elements equal to val.
                        RightW = RightW - 1
                else:
                    LeftW = LeftW + 1
            return Count
        else:
            return 0
