# Approach

When the array length is at least `3`, divide the answer into two cases:

1. **Does not wrap around the ends**: directly find the maximum sum of an ordinary nonempty contiguous subarray, `maxVal`.
2. **Wraps around the ends without covering the entire array**: the selected elements consist of a suffix and a prefix of the array, leaving exactly one nonempty contiguous interval in the middle. Therefore, the maximum sum is `total-minVal`.

The second pass searches for the minimum interval sum only within the index range `[1,n-2]`. This ensures that removing the interval preserves both endpoints of the array, forming a valid circular subarray. The sum of the entire array is already included in the first case.

# Correctness

During the first pass, `preSum` represents the sum from index `0` to the current position, and `minPreSum` stores the smallest previous prefix sum.

The maximum subarray sum ending at the current position is either `preSum`, for a subarray starting at index `0`, or `preSum-minPreSum`. The code updates `maxVal` before updating `minPreSum`, ensuring that the subtraction uses a previous prefix and does not produce an empty interval.

The second pass starts at `nums[1]` and uses the same prefix sum relation to find the minimum interval:

- `preSum` corresponds to an interval starting at index `1`.
- `preSum-maxPreSum` corresponds to the minimum interval obtained by subtracting the largest previous prefix sum.

Again, the answer is updated before the prefix extreme, so `minVal` always corresponds to a nonempty internal interval. The circular interval obtained by removing it is also always nonempty, so the calculation remains valid even when all elements are negative.

These two cases cover all valid subarrays, so the final result is `max(maxVal,total-minVal)`.

When the length is `1` or `2`, the code directly enumerates all possible nonempty subarray sums.

# Complexity

- Time complexity: `O(n)`, with two linear passes.
- Space complexity: `O(1)`, maintaining only prefix sums and extreme values.