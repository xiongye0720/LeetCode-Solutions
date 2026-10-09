# Approach and Correctness

Scan the grid row by row. Whenever a `'1'` is found, increment `cnt` by one and start BFS from that position, traversing the entire island in four directions: up, down, left, and right.

Each land cell is immediately changed to `'0'` when it is enqueued, both marking it as visited and preventing it from being enqueued again. `ops` stores the current level, and `temOps` stores the next level, until the current island has been fully traversed.

Each BFS visits exactly all the land cells in the island containing its starting position. It cannot cross water to reach another island. Therefore, the same island will not be counted again. Each island is counted once when it is first encountered during the scan, so the final `cnt` is the number of islands.

The code modifies the input grid directly. After it finishes, all land cells have been changed to `'0'`.

# Complexity

Let the grid have `m` rows and `n` columns.

- **Time complexity:** `O(mn)`. All positions are scanned, and each land cell is enqueued at most once, with four directions checked each time.
- **Space complexity:** `O(mn)`. The visited state is stored in the grid, and the BFS queues use `O(mn)` space in the worst case.