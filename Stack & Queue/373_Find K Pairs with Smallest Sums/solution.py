class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def cmpParirs(nums1,nums2,k,vers):
            ops = []
            for i in range(min(k,len(nums1))):
                heapq.heappush(ops,(nums1[i]+nums2[0],i,0))
            ans = []
            while k > 0:
                temNode = heapq.heappop(ops)
                if vers == 1:
                    ans.append([nums1[temNode[1]],nums2[temNode[2]]])
                else:
                    ans.append([nums2[temNode[2]],nums1[temNode[1]]])
                if temNode[2] < len(nums2)-1:
                    heapq.heappush(ops,(nums1[temNode[1]]+nums2[temNode[2]+1],temNode[1],temNode[2]+1))
                k = k - 1
            return ans

        if len(nums1) < len(nums2):
            return cmpParirs(nums1,nums2,k,1)
        else:
            return cmpParirs(nums2,nums1,k,2)

        