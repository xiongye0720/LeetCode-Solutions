class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        nRow = len(clips)
        intv = []
        for i in range(nRow):
            temRow = list(clips[i])
            if temRow[1] > time:
                temRow[1] = time
            if temRow[0] < temRow[1]:
                intv.append(temRow)
        intv.sort()

        minIntv = []
        ptr = 0
        right = 0

        while ptr < len(intv):
            if intv[ptr][0] > right:
                return -1
            if intv[ptr][1] > right:
                right = intv[ptr][1]

            if ptr == 0:
                minIntv.append([intv[0]])
            else:
                if len(minIntv[-1]) == 1:
                    if intv[ptr][0] >= minIntv[-1][-1][1]:
                        minIntv.append([intv[ptr]])
                    elif intv[ptr][0] == minIntv[-1][-1][0]:
                        if intv[ptr][1] > minIntv[-1][-1][1]:
                            minIntv[-1] = [intv[ptr]]
                    else:
                        if intv[ptr][1] > minIntv[-1][-1][1]:
                            minIntv[-1].append(intv[ptr])
                else:
                    if intv[ptr][0] >= minIntv[-1][-1][1]:
                        minIntv.append([intv[ptr]])
                    else:
                        if intv[ptr][1] > minIntv[-1][-1][1]:
                            if intv[ptr][0] < minIntv[-1][-2][1]:
                                minIntv[-1].pop()
                                minIntv[-1].append(intv[ptr])
                            elif intv[ptr][0] == minIntv[-1][-2][1]:
                                minIntv[-1].pop()
                                minIntv.append([intv[ptr]])
                            else:
                                minIntv[-1].append(intv[ptr])
            ptr = ptr + 1

        if right < time:
            return -1

        count = 0
        for item in minIntv:
            count = count + len(item)

        return count