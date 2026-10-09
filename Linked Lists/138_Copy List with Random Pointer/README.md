# Approach

The code completes the deep copy in three passes:

1. **Insert copies**: Insert a corresponding new node after each original node, forming the structure `original node → copy → next original node`.
2. **Copy random pointers**: If the random pointer of an original node `res` is not null, `res.random.next` is the copy of the target node, so set `res.next.random = res.random.next`.
3. **Separate the lists**: `res` stores the head of the copied list. `head` and `ptr` advance through the original nodes and copied nodes, respectively, restoring the original list and connecting the copied list. Finally, use `head.next = None` to break the link between the original list's tail and the last copied node.

For an empty list, return `None` directly.

# Correctness

The first pass ensures that each original node is immediately followed by its unique copy with the same value. The second pass uses this correspondence to make each copy's random pointer point to the copy of the target node. If the original random pointer is null, the copy retains the default value `None`.

During separation, the two lists connect the original nodes and copied nodes separately while preserving their original order. Therefore, the returned list has the same values and relationships for both types of pointers as the original list, all its nodes are newly created, and the original list is restored.

# Complexity

Let the linked list have `n` nodes:

- **Time complexity: O(n)**, since all three passes take linear time.
- **Auxiliary space complexity: O(1)**, since only a fixed number of pointers are used; if the newly created copied nodes are included, the total space complexity is **O(n)**.