# Approach

First, use `points.sort()` to sort the balloons by their left endpoints in ascending order.

`ops` represents the common intersection of the current group of balloons, and `count` represents the number of groups formed. Each group requires one arrow.

- If the current balloon's left endpoint is greater than `ops[1]`, the common intersection cannot be extended to include it. Add one arrow and start a new group with the current balloon.
- Otherwise, update `ops` to its intersection with the current balloon, ensuring that the group can still be burst with the same arrow.

The intervals include their endpoints, so a balloon whose left endpoint equals `ops[1]` can still share the same arrow.

# Correctness

Each group always has a nonempty common intersection. Shooting an arrow within that intersection bursts the entire group, so `count` arrows are sufficient.

For each group, choose a balloon with the smallest right endpoint. Its right endpoint is the group's final `ops[1]`. When a new group starts, its first balloon's left endpoint is strictly greater than this right endpoint of the previous group. Since the balloons are sorted, all balloons in the new group have greater left endpoints as well. Therefore, the selected balloons from different groups are pairwise disjoint and require separate arrows.

Thus, at least `count` arrows are needed, so the number returned by the code is minimal.

# Complexity

Let the number of balloons be `n`:

- Time complexity: `O(n log n)`. Sorting dominates, while the traversal takes `O(n)`.
- Space complexity: `O(n)`, due to the auxiliary space used by Python's sorting; the traversal itself requires only `O(1)` extra space.