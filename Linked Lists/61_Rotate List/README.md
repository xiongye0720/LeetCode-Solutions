# Approach

Return directly if the linked list is empty or `k == 0`. Otherwise, traverse the list, use `cnt` to record its length, and leave `ptr` at the tail node.

Update `k` to `k % cnt` to remove full rotation cycles. If the result is zero, return directly.

Then perform the following steps:

1. Connect the tail to the head with `ptr.next = head` to form a cycle.
2. Update `k` to `cnt - k`, which represents the position of the new tail in the original list (starting from 1).
3. Move `k-1` steps from the original head to reach the new tail.
4. Save the new head in `nodeSt`, then break the cycle with `head.next = None`.

# Correctness

Let the length of the linked list be `n`, and let the effective number of rotations be `r = k % n`. Rotating right `r` times moves the last `r` nodes of the original list to the front, so the new tail is the `n-r`th node of the original list.

The code moves `n-r-1` steps from the original head, reaching exactly this node. After the cycle is formed, its successor is the new head. Traversing from there visits the original last `r` nodes, followed by the first `n-r` nodes. Breaking the link at the new tail produces the required rotation.

# Complexity

- **Time complexity:** `O(n)`, since counting the nodes and finding the new tail both require linear traversals.
- **Space complexity:** `O(1)`, since only a fixed number of variables are used.