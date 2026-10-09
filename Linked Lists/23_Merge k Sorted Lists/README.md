# Approach

`ePtr` represents the current number of active linked lists. In each round, merge adjacent lists in pairs:

- Read `lists[2*i]` and `lists[2*i+1]`, and write the merged result to `lists[i]`.
- If the number of lists is odd, move the last list directly to the result region.
- Update `ePtr = (ePtr+1)//2`. The next round processes only the first `ePtr` entries of the array.

When merging two linked lists, use a dummy node `initNode` to handle the head uniformly. At each step, append the smaller of the two current nodes. When one list is exhausted, append the remaining part of the other list directly.

The entire process reconnects the original nodes without copying their values.

# Correctness

Each input linked list is already sorted in ascending order. During merging, the smaller of the two current nodes is also the smallest among all remaining nodes in both lists, so appending nodes one at a time preserves ascending order. The remaining part of the list that has not been exhausted is already sorted and can be appended directly to the tail.

Writing back to `lists[i]` does not overwrite any list that has not yet been read: the current input positions `2*i` and `2*i+1` have already been read, and all later input positions are greater than `i`. In the odd case, the last list is also read before being written back.

Therefore, the active lists produced in each round are all sorted and together contain all original nodes. The number of active lists is halved each round until only one remains, which is a linked list containing all nodes in ascending order.

# Complexity

Let the number of linked lists be `k`, and the total number of nodes be `N`.

- Time complexity: `O(N log k + k)` when `k >= 2`. There are `O(log k)` rounds, each processing at most `O(N)` nodes; the total number of list entries processed across all rounds is `O(k)`. When `k <= 1`, the result is returned directly in `O(1)` time.
- Auxiliary space complexity: `O(1)`. The input array and linked list nodes are reused, with only a fixed number of pointers and temporary dummy nodes.