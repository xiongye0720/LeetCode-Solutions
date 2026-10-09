# Approach

Return directly when `left == right`. Otherwise, use a dummy head node `initNd` to handle cases where the reversal interval starts at the head.

First, move `ptrSt` to the predecessor of the `left`th node. Then set `ptr` to the first node in the interval and `ptr1` to the next node.

During reversal, each round first saves the successor of `ptr1`, then points the current node's `next` to `ptr` and updates `ptr`. After `right-left` operations:

- `ptr` points to the first node of the reversed interval.
- `ptr1` points to the node after the interval.
- `ptrSt.next` still points to the original first node of the interval, which is now its tail.

Finally, first execute `ptrSt.next.next = ptr1` to connect the new tail, then execute `ptrSt.next = ptr` to connect the new head. This order preserves access to the original first node through `ptrSt.next`.

# Correctness

Each reversal step saves the successor first, so changing the links does not lose the unprocessed portion. The loop reverses the links between adjacent nodes in the interval one by one, ultimately reversing the order of the entire interval.

Then, connect the original first node of the interval to the node after the interval, and connect the interval's predecessor to its new first node, restoring the complete linked list. The order of nodes outside the interval remains unchanged, so the result satisfies the requirements.

# Complexity

Let the length of the linked list be `n`:

- **Time complexity:** `O(n)`, since locating and reversing the interval only traverse up to the `right`th node of the original list.
- **Space complexity:** `O(1)`, since only one dummy head node and a fixed number of variables are used.