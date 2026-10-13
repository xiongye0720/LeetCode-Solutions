class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        needs = g
        cookies = s

        if len(cookies) == 0:
            return 0
        else:
            # Process needs and cookies from smallest to largest.
            needs.sort()
            cookies.sort()
            needs = deque(needs)
            cookies = deque(cookies)

            while len(needs) > 0 and len(cookies) > 0:
                if cookies[0] >= needs[0]:
                    # Use the smallest sufficient cookie for this child.
                    cookies.popleft()
                    needs.popleft()
                else:
                    # This cookie cannot satisfy any remaining child.
                    cookies.popleft()

            cnt = len(g) - len(needs)
            return cnt