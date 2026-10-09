class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverseList(OriList,Left,Right):
            # Reverse the inclusive range in place.
            while Left < Right:
                Tem = OriList[Left]
                OriList[Left] = OriList[Right]
                OriList[Right] = Tem
                Left = Left + 1
                Right = Right - 1
        
        # A full rotation leaves the array unchanged.
        Step = k % len(nums)
        if Step > 0:
            # Move the last Step elements to the front in reversed order.
            reverseList(nums,0,len(nums)-1)
            # Restore the order within both parts.
            reverseList(nums,0,Step-1)
            reverseList(nums,Step,len(nums)-1)
