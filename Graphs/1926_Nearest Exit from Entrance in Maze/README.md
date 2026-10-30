# Approach and Correctness

The code uses level-by-level BFS. `ops` stores node coordinates and their distances from the entrance. `visit` marks walls and the entrance in advance to prevent entering walls or revisiting the entrance.

In each round, all nodes in the current level are processed first. Valid, unvisited adjacent positions are collected in `temNodes`, with each dictionary value storing the distance of the position's predecessor. Since these positions are marked as visited only after the current round's collection is complete, `temNodes` removes duplicates to prevent multiple predecessors from adding the same position to the next level.

All nodes in the current level have the same distance, so the distance for the next level is uniformly `temNodes[key] + 1`. If the next level contains a boundary position, this distance is the distance to the nearest exit. Even if multiple exits in this level update `ans` repeatedly, the result remains the same. The entrance is marked in advance, so it will not be treated as an exit. If the queue is exhausted without finding an exit, the code returns `-1`.

# Complexity

Let the maze have `nRow` rows and `nCol` columns.

- **Time Complexity:** `O(nRow × nCol)`. Initialization scans the entire maze. Each reachable position is enqueued at most once, and four directions are checked each time. Dictionary operations take `O(1)` time on average.
- **Auxiliary Space Complexity:** `O(nRow × nCol)`. The space is mainly used for visited markers, the queue, and the dictionary of nodes in the next level.