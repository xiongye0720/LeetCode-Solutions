# Approach

`DFS` uses `valRan` to represent the open interval `(lower bound, upper bound)` that the current node must satisfy.

- The initial range for the root is `(-∞, +∞)`.
- If the current value is not strictly within the range, set the shared flag `isOK[0]` to `False` and return.
- When recursing into the left subtree, keep the lower bound and tighten the upper bound to the current node's value.
- When recursing into the right subtree, keep the upper bound and tighten the lower bound to the current node's value.

If the left subtree check fails, return immediately to avoid checking the right subtree. Finally, return `isOK[0]`.

# Correctness

The range passed through recursion includes all ancestor constraints that the current node must satisfy. Entering the left subtree adds the constraint “less than the current node,” while entering the right subtree adds the constraint “greater than the current node.” Previous constraints are also preserved.

Therefore, if all nodes pass the range check, all values in each node's left subtree are strictly smaller than its value, and all values in its right subtree are strictly greater. The entire tree satisfies the definition of a binary search tree.

Conversely, any node that violates an ordering constraint imposed by an ancestor falls outside the allowed range, making the result `False`. Using open intervals also ensures that equal values cannot pass the check.

# Complexity

Let the number of nodes be `n` and the tree height be `h`.

- **Time complexity:** `O(n)` in the worst case. Each node is checked at most once.
- **Space complexity:** `O(h)` for the recursion stack, which becomes `O(n)` when the tree degenerates into a chain.