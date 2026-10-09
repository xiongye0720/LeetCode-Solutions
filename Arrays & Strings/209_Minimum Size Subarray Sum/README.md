# Approach

Use a sliding window `[left, right)`. `total` stores the sum of the window elements, and `notFound` indicates that the current window sum has not yet reached `target`.

- When `notFound` is true, advance `right` until the window sum reaches the target or the array is exhausted.
- Once the target is reached, update `minLen` using `right-left`, then remove the leftmost element to try to shorten the window.
- If the window sum still reaches the target after shrinking, update the answer directly in the next iteration; otherwise, expand the right endpoint again.
- Stop once a window of length 1 is found. If no window ever reaches the target, return 0.

# Correctness

The problem guarantees that all elements are positive, so expanding the right endpoint increases the window sum, while shrinking the left endpoint decreases it.

For each left endpoint, the code expands only until the window sum first reaches the target. After the left endpoint moves right, shorter windows that previously failed to reach the target have even smaller sums, so the right endpoint does not need to move backward. Thus, each processed left endpoint gives its shortest window that reaches the target, and taking the minimum of these lengths gives the answer.

If the right endpoint has reached the end of the array and the window sum still falls short of the target, further shrinking only decreases the sum, so the loop can end. Length 1 is already the minimum length of a non-empty subarray, so the loop can also end immediately in this case.

# Complexity

Let the array length be `n`.

- **Time complexity:** `O(n)`. Both pointers move only to the right, and each element enters and leaves the window at most once.
- **Space complexity:** `O(1)`. Only a constant number of variables are used.