class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def UpdNode(ndId,segTree,tarNum,tarInt,left,right):
            if tarInt==left and tarInt==right:
                segTree[ndId] = max(tarNum,segTree[ndId])
                return

            if tarInt <= (left+right)//2:
                UpdNode(2*ndId+1,segTree,tarNum,tarInt,left,(left+right)//2)
            else:
                UpdNode(2*ndId+2,segTree,tarNum,tarInt,(left+right)//2+1,right)
            leftInt = segTree[2*ndId+1]
            rightInt = segTree[2*ndId+2]
            segTree[ndId] = max(leftInt,rightInt)

        def QryInt(tarInt,left,right,ndId,segTree):
            if tarInt[0]==left and tarInt[1]==right:
                return segTree[ndId]
            
            mid = (left+right) // 2
            if mid >= tarInt[1]:
                return QryInt(tarInt,left,mid,2*ndId+1,segTree)
            elif mid+1 <= tarInt[0]:
                return QryInt(tarInt,mid+1,right,2*ndId+2,segTree)
            else:
                leftInt = QryInt((tarInt[0],mid),left,mid,2*ndId+1,segTree)
                rightInt = QryInt((mid+1,tarInt[1]),mid+1,right,2*ndId+2,segTree)
                return max(leftInt,rightInt)


        segTree = list(set(nums))
        segTree.sort()
        length = len(segTree)
        numToId = {}
        for i in range(length):
            numToId[segTree[i]] = i
        segTree = [-1] * (4*length)

        dp = [(1,-1)]
        UpdNode(0,segTree,1,numToId[nums[0]],0,length-1)

        for i in range(1,len(nums)):
            plan2 = max(dp[-1][0],dp[-1][1])
            if numToId[nums[i]] == 0:
                plan1 = 1
            else:
                plan1 = QryInt((0,numToId[nums[i]]-1),0,length-1,0,segTree)
                if plan1 == -1:
                    plan1 = 1
                else:
                    plan1 = plan1 + 1
            UpdNode(0,segTree,plan1,numToId[nums[i]],0,length-1)
            dp.append((plan1,plan2))

        return max(dp[-1][0],dp[-1][1])