# Approach and Correctness

The code uses an explicit stack to simulate depth-first traversal. Each stack frame stores a node, the index of the child currently being processed, and the total number of children.

When the node at the top of the stack still has unprocessed children, the corresponding child is pushed onto the stack. Its depth is determined by the stack length, and its value is added to `levels`. When all children of the node at the top of the stack have been processed, the node is popped. The parent's child index is then incremented by one to continue with the next child.

The stack always stores the path from the root to the current node, so `len(stack)` accurately represents the current depth. Each node is recorded exactly once, and subtrees are traversed in the order of `children`, ensuring that nodes at the same depth are added from left to right. Finally, the lists in `levels` are collected in order of depth to obtain the level order traversal.

# Complexity

Let `n` be the number of nodes and `H` be the height of the tree.

- **Time Complexity:** `O(n)`. Each node is pushed onto and popped from the stack once, and the `H` levels are collected at the end. Dictionary operations take `O(1)` time on average.
- **Auxiliary Space Complexity:** `O(H)`. The stack stores at most `H` stack frames, and the `levels` dictionary contains `H` entries. The lists for each level are directly referenced by `ans` and are part of the returned result. Including the returned result, the total space complexity is `O(n)`.