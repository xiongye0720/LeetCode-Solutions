# Approach

All elements in the array are distinct.

If `nums[0] <= nums[-1]`, the array is in ascending order, so return the first element directly.

Otherwise, the array consists of two ascending segments: all elements in the first segment are greater than or equal to `nums[0]`, and all elements in the second segment are less than `nums[0]`. The minimum is the first element of the second segment.

During binary search:

- If `nums[mid] >= nums[0]`, `mid` is in the first segment, so set `left = mid`.
- Otherwise, `mid` is in the second segment, so set `right = mid`.

When the two boundaries are adjacent, return `nums[right]`.

# Correctness

Let `p` be the index of the minimum. Initially, `left` is in the first segment and `right` is in the second segment, satisfying `left < p <= right`.

If `mid` is in the first segment, then `mid < p`, so the relation still holds after updating `left`. If `mid` is in the second segment, then `p <= mid`, so the relation also holds after updating `right`.

The interval keeps shrinking until `right-left == 1`. At this point, `p == right` must hold, so the returned value is correct.

# Complexity

- **Time complexity:** `O(log n)`, since the binary search interval shrinks by about half in each iteration; `O(1)` when returning directly.
- **Space complexity:** `O(1)`, using only a fixed number of variables.