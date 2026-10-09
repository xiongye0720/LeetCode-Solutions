# Approach

The first pass traverses from right to left. Using `answer[ptr-1] = answer[ptr] * nums[ptr]`, it makes `answer[i]` store the product of all elements to the right of `nums[i]`. The last position has no elements to its right, so it keeps the initial value `1`.

The second pass traverses from left to right, using `preMul` to accumulate the product of all elements to the left of the current position, then multiplying it into `answer[ptr]`. The first position has no elements to its left, so no update is needed.

For each position, the final result is the product of its left-side and right-side products, which includes exactly all elements except itself. The entire process uses no division and also works when the array contains zeros.

# Complexity

- Time complexity: `O(n)`, since the array is traversed twice.
- Space complexity: the returned array uses `O(n)` space. Excluding the returned array, the extra space is `O(1)`.