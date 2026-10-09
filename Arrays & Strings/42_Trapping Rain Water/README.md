# Approach

`cntr` stores the heights of bars that have not yet been processed, with the front of the deque serving as the left boundary. `count` accumulates the amount of trapped water.

1. **Scan from left to right**  
   The initial `-1` is replaced by the first bar. If a subsequent bar is lower than the front of the deque, append it to the back. When a bar is at least as high as the front, both boundaries are in place. Use the left boundary height `temHt` as the water level, add `temHt - height` for each interior bar, and then make the current bar the new left boundary.

2. **Process the remaining part from right to left**  
   After the scan, the front of the deque is a globally tallest bar, and all remaining bars are lower than it. Pop the back of the deque as the right boundary `temHt`. For consecutive lower bars to its left, add `temHt - height` to the trapped water total and remove them. Stop when reaching a bar that is at least as high as `temHt`, then use this taller or equally tall bar to continue processing in the next iteration.

# Correctness

In the first stage, the front of the deque is a tallest bar in the scanned portion, and all interior bars are lower than it. Once a right boundary at least as high as the front is found, the water level at each interior position is exactly the left boundary height, so the calculation is accurate.

In the second stage, a globally tallest bar always serves as the boundary on the left, while `temHt` is the maximum height on the right side of the portion currently being processed. Therefore, the water level for consecutive bars lower than `temHt` is exactly `temHt`. When a taller or equally tall bar is reached, it becomes the new right boundary. The front of the deque is high enough to ensure that the inner loop stops.

The interior bars processed in the two stages do not overlap, and the trapped water at each bar is calculated only once, so no water is missed or counted twice.

# Complexity

Let the number of bars be `n`.

- **Time complexity:** `O(n)`. Each bar is added to the deque once and removed from the front or back at most once, so the total number of operations in the nested loops is still linear.
- **Space complexity:** `O(n)`. In the worst case, `cntr` stores the heights of all bars.