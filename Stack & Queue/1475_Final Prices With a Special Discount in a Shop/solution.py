class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        price = prices
        nextIdx = [-1] * len(price)

        right = len(price) - 2
        while right >= 0:
            temPtr = right + 1
            isFound = True
            while price[right] < price[temPtr]:
                if nextIdx[temPtr] == -1:
                    isFound = False
                    break
                temPtr = nextIdx[temPtr]
            if isFound:
                nextIdx[right] = temPtr
            right = right - 1

        resList = []
        for i in range(len(price)):
            if nextIdx[i] == -1:
                resList.append(price[i])
            else:
                resList.append(price[i] - price[nextIdx[i]])

        return resList