# Approach

Use postorder DFS to compute the subtree states before processing the current node. Each node returns two states:

- `dp[0]`: the maximum sum of a path that starts at the current node and extends downward. It may contain only the current node.
- `dp[1]`: the maximum sum of a path that passes through the current node and enters both the left and right subtrees. If either subtree is missing, this state is negative infinity.

`dp[0]` starts with `tNode.val`, then tries connecting to the left or right child's `dp[0]` and takes the maximum. Therefore, it chooses at most one direction and can still connect to the parent node.

When both children exist:

`dp[1] = tNode.val + dpLeft[0] + dpRight[0]`

This path already connects both sides and cannot extend to the parent node, as that would create a branch. Therefore, the parent only uses each child's `dp[0]`.

After processing each node, use both states to update the shared `maxVal[0]`.

# Correctness

Every valid path has a unique highest node. Relative to that node, the path has only two possible forms:

- It contains only that node or extends to one side, which is covered by `dp[0]`.
- It enters both the left and right subtrees, which is covered by `dp[1]`.

The maximum one-sided paths returned by the subtrees provide the best choices for each side. Therefore, these two states cover all paths whose highest node is the current node. Traversing all nodes and updating the global maximum gives the answer for the entire tree, including paths that do not pass through the root.

`dp[0]` always keeps the current node itself as an option, so subpaths with negative contributions can be discarded. Even if all node values are negative, the answer is still the largest single-node value, and an empty path is never incorrectly selected.

# Complexity

Let the number of nodes be `n` and the tree height be `h`:

- Time complexity: `O(n)`. Each node is processed once.
- Space complexity: `O(h)` for the recursive call stack and the constant-sized states stored at each level; `O(n)` in the worst case.