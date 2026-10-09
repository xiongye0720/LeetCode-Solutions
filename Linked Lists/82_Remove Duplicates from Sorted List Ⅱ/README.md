# Approach

Use a dummy head node `nodeSt` to handle cases where nodes at the head are removed. `ptr` points to the last node confirmed to be kept and initially points to the dummy head; `ptr1` scans the current group of nodes with the same value.

In each round, use the inner loop to count the nodes in the current group as `cnt`, leaving `ptr1` at the end of the group:

- If `cnt == 1`, keep the node, move `ptr` to it, and then advance `ptr1`.
- If `cnt > 1`, move `ptr1` to the start of the next group, then skip the entire group with `ptr.next = ptr1`. Keep `ptr` in place.

Finally, return `nodeSt.next`.

# Correctness

The linked list is sorted, so nodes with the same value must be consecutive. The inner loop therefore identifies each complete group of nodes with the same value.

A group with one node represents a value that appears only once, so the code keeps it. A group with more than one node represents a repeated value, so the code removes the entire group by changing the predecessor's link.

Each group is processed exactly once, and the relative order of the retained nodes remains unchanged. Therefore, the final list contains exactly all nodes whose values appear only once in the original list.

# Complexity

Let the length of the linked list be `n`:

- **Time complexity:** `O(n)`. `ptr1` always moves forward, and each node is scanned only once.
- **Space complexity:** `O(1)`. Only one dummy head node and a fixed number of variables are used.