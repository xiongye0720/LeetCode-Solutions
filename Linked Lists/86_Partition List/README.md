# Approach

`nodeDown` is the dummy head of the original list, and `ptrDown` points to the predecessor of the node currently being processed. `nodeUp` and `ptrUp` are used to collect nodes with values greater than or equal to `x`.

During traversal:

- If `head.val >= x`, remove the current node from the original list with `ptrDown.next = head.next`, then append it after `ptrUp`. Keep `ptrDown` in place so it remains the predecessor of the next node to be processed.
- If `head.val < x`, keep the current node and move `ptrDown` to it.

After traversal, first use `ptrUp.next = None` to clear the tail node's remaining link to the original list, then connect the retained portion to `nodeUp.next`.

# Correctness

During traversal, processed nodes with values less than `x` remain in the original list in their original order. Nodes with values greater than or equal to `x` are appended to another list in the order they are encountered. Therefore, the relative order within each portion remains unchanged.

Each node is processed exactly once and ends up in its corresponding portion. After breaking the link at the tail of the second portion, joining the two portions ensures that all nodes with values less than `x` appear before the remaining nodes and that the list terminates correctly.

# Complexity

Let the length of the linked list be `n`:

- **Time complexity:** `O(n)`, since the list is traversed only once.
- **Space complexity:** `O(1)`, since only two dummy head nodes and a fixed number of pointer variables are used.