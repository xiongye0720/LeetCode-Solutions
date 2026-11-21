# Approach and Correctness

The code caps each segment's end at `time`, filters out zero-length segments, and sorts them by start position. `right` tracks the farthest position continuously covered by the segments scanned so far. If the current segment starts after `right`, later segments cannot start any earlier, so the gap cannot be filled, and the code returns `-1`.

`minIntv` stores the retained segments in groups. Consecutive segments within each group strictly overlap, and adjacent groups meet exactly at their endpoints. During the scan, segments that cannot extend the current chain's coverage are ignored. If a segment can extend the coverage and has the same start as the last segment, it directly replaces the last segment. In other cases, the code checks whether it can connect to the second-to-last segment. If so, it replaces the old last segment. Otherwise, it is appended. When endpoints meet exactly, a new group is created to maintain this structure.

Every prefix of the retained chain reaches the farthest position that can be continuously covered with that number of segments. Replacing the last segment extends coverage without increasing the number of segments. If a new segment starts after the end of the second-to-last segment, the coverage obtained using one fewer segment cannot connect to it, so the number of segments must increase. Therefore, these updates always maintain the minimum number of segments.

Finally, if `right < time`, the end is still uncovered, so the code returns `-1`. Otherwise, the sum of all group lengths is the answer.

# Complexity

Let `n` be the number of input segments.

- **Time Complexity:** `O(n log n)`. Sorting dominates, while preprocessing, scanning, and the final count each take `O(n)`.
- **Auxiliary Space Complexity:** `O(n)`. The space is used to store `intv` and `minIntv`, as well as temporary storage needed for sorting.