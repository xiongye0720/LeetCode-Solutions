class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt1 = {}
        for item in nums1:
            cnt1[item] = cnt1.get(item,0) + 1

        cnt2 = {}
        for item in nums2:
            cnt2[item] = cnt2.get(item,0) + 1

        res = {}
        for key in cnt1:
            if key in cnt2:
                freq = min(cnt1[key],cnt2[key])
                if freq in res:
                    res[freq].append(key)
                else:
                    res[freq] = [key]

        if len(res) == 0:
            return []
        else:
            res = list(res.items())
            ans = []
            for item in res:
                temNums = item[1]
                for num in temNums:
                    for i in range(item[0]):
                        ans.append(num)
            return ans