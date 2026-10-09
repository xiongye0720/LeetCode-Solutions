# Approach

The code traverses the current level using its existing `next` chain while building the `next` chain for the next level.

At the start of each level, create a dummy node `temNode` and let `temPtr` point to it. Then traverse the current level along `ptrSt.next`, appending each node's existing left and right children to `temPtr` in that order and advancing the tail pointer.

After the current level is processed, `temNode.next` is the first node of the next level. Assign it to `ptrSt` and continue until there is no next level. Finally, return the original root node.

# Correctness

The root forms a level by itself, so its `next` chain is already correct.

If the current level's `next` chain connects nodes from left to right, traversing the parent nodes along this chain and appending their left and right children in order connects all nodes in the next level from left to right. Missing children are skipped without affecting the order.

The problem guarantees that all `next` pointers are initially `None`, so the last node in each level keeps its `next` pointer as `None`. Repeating this process level by level correctly connects the entire tree. An empty tree returns `None` directly.

# Complexity

Let the tree contain `N` nodes.

- **Time complexity:** `O(N)`. Each node is traversed once, and each child node is connected once.
- **Space complexity:** `O(1)`. Only a fixed number of pointers and temporary dummy nodes are used. Dummy nodes from different levels are not retained cumulatively.