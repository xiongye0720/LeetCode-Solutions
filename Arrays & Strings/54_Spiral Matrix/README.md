# Approach

Start at `(0,0)` and move in the order right→down→left→up. `dirStr` stores the current direction, and `Pt` stores the next coordinate to visit.

At each visit, append the element to `resList`, then set its original position to `None` to mark it as visited. If the next position in the current direction is out of bounds or already visited, turn clockwise; otherwise, continue forward. Stop the traversal when the coordinate retrieved in the next iteration cannot be visited.

This code modifies the original matrix. After the traversal, all elements are `None`.

# Correctness

All elements in the problem are integers, so `None` clearly identifies visited positions and prevents duplicate output.

Starting from the top-left corner and moving right, the traversal turns clockwise whenever it reaches a matrix boundary or a visited position. This visits the top, right, bottom, and left edges of the current layer in order. After the outer layer is completed, the visited positions form new boundaries, allowing the path to naturally enter the inner layer.

As long as unvisited elements remain, the path can continue through the remaining region. Once all elements have been visited, the next coordinate is out of bounds or already visited, and the loop ends. Therefore, each element is output exactly once in spiral order.

# Complexity

Let the matrix have `m` rows and `n` columns.

- **Time complexity:** `O(mn)`. Each element is visited once, and each step performs only a constant number of checks.
- **Extra space complexity:** `O(1)`, excluding the returned result. In each iteration, one coordinate is removed from `Pt` and one is added, so it stores at most one coordinate. Visited markers are written directly into the original matrix.
- **Result space:** `O(mn)`, for storing all elements.