# Approach and Correctness

First, sort the positions in place, then perform binary search on the minimum distance between balls.

For a candidate distance `mid`, place the first ball at `loc[0]`. Then repeatedly find the leftmost position that is at least `mid` away from the previous ball, attempting to place the remaining `m - 1` balls. Placing each ball as early as possible leaves as much space as possible for later balls. Therefore, if this approach cannot place all the balls, no other placement can satisfy this distance.

A feasible distance remains feasible when reduced, so binary search can be used. Initially, `left = 0` is feasible, while `right = loc[-1] - loc[0] + 1` exceeds the entire range of positions and must be infeasible. Each round updates the endpoints based on the check result, keeping the left endpoint feasible and the right endpoint infeasible. When the two endpoints are adjacent, `left` is the maximum feasible distance.

# Complexity

Let `n` be the number of positions and `D` be the difference between the largest and smallest positions.

- **Time Complexity:** `O(n log n + n log(D + 1))`. Sorting takes `O(n log n)`. During each feasibility check, the scan keeps moving to the right, and the scanned segments overlap only at their endpoints. Therefore, each round still takes `O(n)`, even with nested loops.
- **Auxiliary Space Complexity:** `O(n)`. Python's sort requires linear temporary space in the worst case. The binary search and placement check themselves use only a fixed number of variables.