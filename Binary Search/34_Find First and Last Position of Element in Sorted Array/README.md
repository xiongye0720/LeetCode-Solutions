# Approach

The code first handles an empty array and a target outside the array's value range, then classifies the remaining cases based on the first and last elements:

- Both endpoints equal `target`: the entire array contains the target value, so return the indices of both endpoints directly.
- The first element is less than `target` and the last element is greater than `target`: use binary search to find the left and right boundaries separately.
- The first element equals `target`: the left boundary is already known to be `0`, so only search for the right boundary.
- Otherwise: the last element equals `target`, so the right boundary is already known to be the last index, and only the left boundary needs to be found.

Both binary searches end when `right-left == 1`:

- **Find the left boundary**: move `left` when an element is less than the target; otherwise, move `right`. When the search ends, `right` is the first position whose value is greater than or equal to the target. If this element is greater than the target, the target does not exist.
- **Find the right boundary**: move `left` when an element is less than or equal to the target; otherwise, move `right`. When the search ends, `left` is the last position whose value is less than or equal to the target. If the target exists, this is its last occurrence.

# Correctness

The array is sorted, so all occurrences of the target must be consecutive.

The search for the left boundary always maintains `nums[left] < target <= nums[right]`, while the search for the right boundary always maintains `nums[left] <= target < nums[right]`. Each update preserves the corresponding relation and narrows the interval. When the two indices become adjacent, the required boundary is determined.

The endpoint classification ensures that the corresponding conditions hold at the start of each binary search. It also directly handles cases where a boundary is at either end of the array. Therefore, the code returns the full consecutive interval containing the target, or `[-1,-1]` if the target does not exist.

# Complexity

Let `n` be the length of the array:

- **Time complexity: O(log n)**, with at most two binary searches.
- **Space complexity: O(1)**, using only a fixed number of variables.