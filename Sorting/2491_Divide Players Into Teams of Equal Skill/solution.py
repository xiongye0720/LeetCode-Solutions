class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        nums = skill

        total = 0
        freq = {}

        for item in nums:
            total = total + item
            if item in freq:
                freq[item] = freq[item] + 1
            else:
                freq[item] = 1

        teamSums = []
        cnt = len(nums) // 2
        if total % cnt == 0:
            teamSums.append(total // cnt)

        if teamSums == []:
            return -1
        else:
            isFound = False
            teamSum = 0
            for item in teamSums:
                isOk = True
                for key in freq:
                    if item-key in freq:
                        if item-key == key:
                            if freq[key] % 2 != 0:
                                isOk = False
                                break
                        else:
                            if freq[key] != freq[item-key]:
                                isOk = False
                                break
                    else:
                        isOk = False
                        break
                if isOk:
                    isFound = True
                    teamSum = item
                    break

            if isFound:
                ans = 0
                for key in freq:
                    ans = ans + key * (teamSum-key) * freq[key]
                return ans // 2
            else:
                return -1