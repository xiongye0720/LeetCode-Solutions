class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m!=0 and n!=0:
            Ptr1 = m - 1
            Ptr2 = n - 1
            Ptr = m + n - 1
            # Merge backward to avoid overwriting unread elements in nums1.
            while Ptr >= 0:
                if Ptr1>=0 and Ptr2>=0:
                    # Place the larger remaining element at Ptr.
                    if nums1[Ptr1] >= nums2[Ptr2]:
                        nums1[Ptr] = nums1[Ptr1]
                        Ptr1 = Ptr1 - 1
                        Ptr = Ptr -1
                    else:
                        nums1[Ptr] = nums2[Ptr2]
                        Ptr2 = Ptr2 - 1
                        Ptr = Ptr - 1
                elif Ptr1<0 and Ptr2>=0:
                    nums1[Ptr] = nums2[Ptr2]
                    Ptr2 = Ptr2 - 1
                    Ptr = Ptr - 1
                elif Ptr1>=0 and Ptr2<0:
                    # Remaining nums1 elements are already in their final positions.
                    Ptr1 = Ptr1 - 1
                    Ptr = Ptr -1
        elif m==0 and n!=0:
            for i in range(n):
                nums1[i] = nums2[i]