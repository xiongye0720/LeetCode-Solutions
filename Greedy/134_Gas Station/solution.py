class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)

        left = 0
        while left < length:
            temPtr = left
            total = 0
            while temPtr-left < length:
                total = total + gas[temPtr%length] - cost[temPtr%length]
                if total < 0:
                    break
                temPtr = temPtr + 1
            if temPtr-left == length:
                return left
            left = temPtr + 1
        
        return -1
                    

        