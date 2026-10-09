# Approach

`ops` stores the nodes in the current level. Nodes are always removed using `popleft()`, and their values are added to `temRow`. `isOdd` controls the traversal direction for the current level:

- When it is `True`, traverse the current level from left to right, adding the left child and then the right child to `temOps` using `appendleft()`.
- When it is `False`, traverse the current level from right to left, adding the right child and then the left child to `temOps` using `appendleft()`.

After each level, save `temRow`, switch the direction, and use `temOps` as the queue for the next level. For an empty tree, return an empty list directly.

# Correctness

`appendleft()` places nodes added later at the front, reversing both the order of child groups from different parent nodes and the order of children from the same parent node.

When the current level is traversed from left to right, adding the left child before the right child arranges the next level from right to left. When the current level is traversed from right to left, adding the right child before the left child arranges the next level from left to right.

The root level follows the initial direction, and each subsequent level generates the next level in the opposite direction. Therefore, the result satisfies the requirements of zigzag traversal.

# Complexity

Let the total number of nodes be `N` and the maximum width of the tree be `W`.

- **Time complexity:** `O(N)`. Each node is enqueued and dequeued once.
- **Auxiliary space complexity:** `O(W)`. This is used for the current-level queue, the next-level queue, and the current level's result. Including the returned result, the total space complexity is `O(N)`.