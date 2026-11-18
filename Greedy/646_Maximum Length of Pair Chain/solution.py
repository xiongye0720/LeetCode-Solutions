class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        nRow = len(pairs)
        intv = []

        for i in range(nRow):
            temRow = pairs[i]
            intv.append((temRow[0], temRow[1]))

        intv.sort()

        lastIntv = None
        count = 0

        for item in intv:
            if lastIntv is None:
                lastIntv = item
                count = count + 1
            else:
                if item[0] > lastIntv[1]:
                    lastIntv = item
                    count = count + 1
                else:
                    if item[1] < lastIntv[1]:
                        lastIntv = item

        return count