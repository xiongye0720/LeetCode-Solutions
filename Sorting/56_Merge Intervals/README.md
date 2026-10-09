# Approach

`intervals.sort()` sorts the intervals by their left endpoints in ascending order. Then process them one by one:

- If `res` is empty, add the current interval directly.
- If `item[0] > res[-1][1]`, the two intervals do not overlap, so append the current interval.
- Otherwise, the two intervals overlap. Update the right endpoint of the last interval to the maximum of their right endpoints.

Intervals with equal endpoints also need to be merged, so a strict greater-than comparison is used to check for non-overlap.

# Correctness

During traversal, `res` remains sorted and contains non-overlapping intervals that exactly cover all processed intervals.

The left endpoint of the current interval is no smaller than the left endpoints of previous intervals. Also, the right endpoints of earlier intervals in `res` are smaller than the left endpoint of the last interval. Therefore, the current interval can only overlap with `res[-1]`.

If there is no overlap, append the current interval directly. If there is an overlap, keep the left endpoint and extend the right endpoint. Both operations preserve the properties above. Therefore, when traversal ends, the result fully covers all intervals without overlap.

# Complexity

Let the number of intervals be `n`:

- Time complexity: `O(n log n)`. Sorting dominates, while traversal takes `O(n)`.
- Space complexity: `O(n)`. The result list and the auxiliary space used by Python's sorting each take at most `O(n)` space.