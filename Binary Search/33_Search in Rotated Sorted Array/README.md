# Approach

The code finds the target position in two steps:

1. **Select a sorted interval**
   - If `nums[-1] < nums[0]`, the array has a rotation boundary. Binary search places `left` at the end of the first segment and `right` at the start of the second segment.
   - Use the first and last values of the two segments to determine which segment may contain the target, and set `posStart` and `posEnd`. If neither segment can contain the target, return `-1`.
   - If the array is not rotated, directly check whether the target is within the value range of the entire array.

2. **Perform binary search within the interval**
   - If the last value in the interval equals the target, return `posEnd` directly.
   - Otherwise, move `left` when an element is less than or equal to the target, and move `right` when an element is greater than the target. Once the two pointers are adjacent, check whether `nums[left]` equals the target.

# Correctness

The original array is strictly increasing. After rotation, it contains at most two increasing segments. When the array is rotated, all elements in the first segment are greater than or equal to `nums[0]`, and all elements in the second segment are less than `nums[0]`. The first binary search always keeps `left` in the first segment and `right` in the second segment, so it finds the boundary exactly when the two pointers become adjacent.

The value ranges of the two segments do not overlap. Therefore, if the target exists, it can only belong to the interval selected using the first and last values.

After selecting the interval, the code has already ensured that the target lies between its first and last values. If the last value is greater than the target, the second binary search always maintains:

`nums[left] <= target < nums[right]`

When the search ends, `left` is the last position in the interval whose value is less than or equal to the target. Therefore, if the value at this position does not equal the target, the target does not exist. Otherwise, return its index.

# Complexity

Let `n` be the length of the array:

- **Time complexity: O(log n)**, with at most two binary searches.
- **Space complexity: O(1)**, using only a fixed number of variables.