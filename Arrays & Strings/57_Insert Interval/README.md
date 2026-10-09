# Approach

The original intervals are sorted by their left endpoints and do not overlap. The code scans them sequentially using `ptr` and builds `res` in two stages.

The first stage determines where to insert the new interval:

- The current interval lies entirely to the left of the new interval: append it directly to `res` and continue scanning.
- The new interval lies entirely to the left of the current interval: append the new interval and exit the loop, leaving `ptr` unchanged so that the second stage can process the current interval.
- The two intervals overlap: take the minimum of their left endpoints and the maximum of their right endpoints, append the merged interval, and move `ptr` to the next interval.

`isInsert` indicates that the new interval has been added to the result or included in a merged interval. If it has not been inserted by the end of the scan, it belongs at the end. This also covers the case where the original list is empty.

The second stage processes the remaining intervals: if the current interval overlaps with `res[-1]`, extend the right endpoint of the last interval; otherwise, append the current interval directly. Equal endpoints also count as an overlap.

# Correctness

All intervals appended directly in the first stage lie to the left of the new interval, so they do not need to be merged. The first insertion or merge also keeps the result sorted and non-overlapping.

In the second stage, the remaining intervals appear in increasing order of their left endpoints, so the current interval can only overlap with the last interval in the result. If they overlap, updating the right endpoint fully covers both intervals. If they do not overlap, appending the current interval keeps the result sorted and non-overlapping.

Therefore, the final result exactly covers all original intervals and the new interval, while remaining sorted and non-overlapping.

# Complexity

Let the number of original intervals be `n`:

- Time complexity: `O(n)`. Both loops share the monotonically increasing `ptr`, and each original interval is processed only once.
- Space complexity: `O(n)`, for the result list. Excluding the returned result, the extra space is `O(1)`.