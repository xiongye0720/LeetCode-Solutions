# Approach

The code traverses the tree in preorder: “current node → left subtree → right subtree,” connecting each node to the tail of the linked list.

- `lastNode[0]` stores the current tail node. It initially points to the auxiliary node `initNode`, allowing the root to use the same connection operation.
- First, save the current node's original `leftChild` and `rightChild` so that later pointer changes do not affect traversal of the original tree.
- Clear the previous tail node's `left` pointer, set its `right` pointer to the current node, and make the current node the new tail.
- Using the saved child references, recursively traverse the left subtree and then the right subtree.

All original nodes are connected directly, and the final linked list still starts at `root`. The auxiliary node is not part of the result.

# Correctness

Whenever a node is visited, `lastNode[0]` is the previously visited node in preorder traversal. The connection operation sets its right pointer to the current node, so the final right chain follows exactly the preorder traversal order of the original tree.

Saving the original child references ensures that all nodes in the original tree remain reachable during traversal, even if the connection process overwrites their left and right pointers. Each node is visited exactly once.

Every node except the last has its left pointer cleared when its successor is connected. The last node in preorder traversal must be a leaf in the original tree, so both of its pointers are already null. Therefore, all left pointers are null in the final result, and the right chain terminates correctly.

# Complexity

Let the number of nodes be `n` and the height of the original tree be `h`.

- **Time complexity:** `O(n)`. Each node is visited once, and each connection operation takes constant time.
- **Space complexity:** `O(h)` for the recursion stack. The auxiliary node and `lastNode` use only constant space. When the tree degenerates into a chain, the space complexity is `O(n)`.