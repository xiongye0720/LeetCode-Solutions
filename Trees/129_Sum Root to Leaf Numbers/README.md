# Approach

Use depth-first search to traverse the binary tree:

- `nums[0]` stores the number represented by the current path. When entering a node, append its value using `nums[0]*10 + root.val`.
- When reaching a leaf node, add the complete path number to `total[0]`.
- Before leaving a node, undo its contribution using `(nums[0]-root.val) // 10` to restore the parent node's path number.

`nums` and `total` use single-element lists so that all recursive calls can modify the same shared state. The path number must be restored during backtracking, while the accumulated result is always retained.

# Correctness

Before entering the current node, `nums[0]` represents the path number from the root to the parent node. After appending the current node's value, it represents the path number from the root to the current node. Therefore, the number added at a leaf node is the complete number represented by that path.

Before each recursive call returns, the path number is restored to its value before entering the node, so traversing different branches does not affect one another. Every leaf node is visited exactly once, so the final `total[0]` is the sum of all root-to-leaf path numbers.

# Complexity

Let the number of nodes be `n` and the tree height be `h`:

- **Time complexity:** `O(n)`. Each node is visited once.
- **Space complexity:** `O(h)`, mainly for the recursive call stack. The two single-element lists use `O(1)` space.