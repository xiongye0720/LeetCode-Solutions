# Approach

The code starts BFS from the `'O'` cells on all four boundaries to find every `'O'` connected to a boundary. These cells must be preserved.

BFS expands in four directions: up, down, left, and right. Each discovered cell is immediately changed to `None` when it is enqueued. This marker indicates that the cell must be preserved and prevents it from being enqueued again. `ops` and `temOps` store the positions in the current and next levels, respectively.

Finally, traverse the entire board, restoring `None` to `'O'` and changing the remaining `'O'` cells to `'X'`.

# Correctness

An `'O'` region is not surrounded if and only if it is connected to an `'O'` on the boundary.

BFS starting from all boundary `'O'` cells marks exactly the cells that satisfy this condition. Therefore, restoring `None` preserves all regions that are not surrounded. Unmarked `'O'` cells are not connected to the boundary and should be changed to `'X'`.

Marking each cell immediately when it is enqueued ensures that each cell is processed at most once. Even if the boundary scan encounters the same region again, it will not repeat the search.

# Complexity

Let the board have `m` rows and `n` columns.

- **Time complexity:** `O(mn)`. Each cell participates in BFS at most once, with four directions checked each time, followed by a traversal of the entire board.
- **Space complexity:** `O(mn)`. Cells are marked directly on the board, but the BFS queues still require `O(mn)` space in the worst case.