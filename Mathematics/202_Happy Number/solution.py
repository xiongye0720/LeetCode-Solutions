class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while True:
            total = 0
            # Compute the sum of the squares of all digits.
            while True:
                quot = n // 10
                rem = n % 10
                total = total + rem * rem
                if quot == 0:
                    break
                n = quot

            if total == 1:
                return True
            elif total in visit:
                # A repeated sum means the process has entered a cycle.
                return False
            
            # Record the sum and use it as the next number.
            visit.add(total)
            n = total
