# Approach

First, perform level-order BFS. Use `father` to store a mapping from each node's `id` to its parent, and record the two target nodes and their depths in `ans`. Stop the search after finding both targets.

Since BFS visits nodes in increasing order of depth, the depth of `ans[0]` is no greater than that of `ans[1]`. The code reassigns them to `p` and `q`, respectively.

If their depths differ, first move `q` upward until it is one level deeper than `p`:

- If the parent of `q` is `p`, return `p` directly.
- Otherwise, move `q` up one more level so that the two nodes have the same depth.

Then move both nodes upward together and return the node where they first meet.

# Correctness

BFS records each node's parent when the node is discovered. Therefore, once both targets are found, their complete parent chains to the root have been established.

Moving the deeper node upward only skips positions that are too deep to be common ancestors. If this process confirms that the shallower node is its ancestor, that node is the lowest common ancestor.

Otherwise, the two nodes remain distinct after their depths are aligned. Moving them upward together checks their ancestors in decreasing order of depth, so the first node where they meet is their deepest common ancestor.

# Complexity

Let the total number of nodes be `N` and the tree height be `H`.

- **Time complexity:** `O(N)`. BFS traverses the entire tree in the worst case. Searching upward takes `O(H)`, and `H ≤ N`.
- **Space complexity:** `O(N)`. This is used for the parent mapping and the BFS queue.