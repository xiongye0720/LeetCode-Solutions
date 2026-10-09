# Approach

Return directly when `k == 1`. Otherwise, use a dummy head node `nodeSt`, and keep `ptrL` pointing to the node immediately before the group to be processed.

Each round consists of three steps:

1. Starting from `ptrL.next`, check whether there are `k` nodes. If there are fewer, stop and preserve the original order of the remaining nodes.
2. Reset `ptrM` to the first node in the group, and set `ptrN` to the second node. At each step, save the successor of `ptrN` before pointing the current node to `ptrM`, gradually reversing the links within the group. After completion, `ptrM` is the new head of the group, and `ptrN` is the start of the next group.
3. Use `temPtr` to save the original head of the group, which becomes its tail after reversal. Connect the group tail to `ptrN`, connect `ptrL` to the new group head, and then move `ptrL` to the new group tail.

# Correctness

At the start of each round, all complete groups before `ptrL` have been correctly reversed, and `ptrL.next` points to the unprocessed portion.

The length check ensures that only complete groups of `k` nodes are reversed. During reversal, the successor is saved before the link is modified, so no subsequent nodes are lost. After `k-1` operations, the order of the nodes in the group is fully reversed. The previous portion, the current group, and the remaining portion are then reconnected, keeping the linked list connected and restoring the state needed for the next round.

When fewer than `k` nodes remain, the process stops immediately, so the remaining portion keeps its original order. The final result therefore satisfies the problem requirements.

# Complexity

Let the length of the linked list be `n`:

- **Time complexity:** `O(n)`. Each complete group is checked once and reversed once, while the remaining portion is checked only once.
- **Space complexity:** `O(1)`. Only one dummy head node and a fixed number of pointer variables are used.