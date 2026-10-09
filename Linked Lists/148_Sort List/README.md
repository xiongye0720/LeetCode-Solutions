# Approach

First, count the total number of nodes, then treat each node as a sorted run of length `1`. In each round, merge adjacent pairs of sorted runs and double `length` until only one sorted run remains.

Variable meanings:

- `length`: The maximum length of each sorted run in the current round; only the last run may be shorter.
- `nums`: Initially represents the number of nodes, then represents the current number of sorted runs.
- `total`: Always stores the total number of nodes in the outer loop; after being passed to `MergeLists`, it is used to calculate the number of unprocessed nodes.

Each round merges `nums // 2` pairs of sorted runs. If the number of runs is odd, the last run remains unchanged; the number of runs in the next round is `(nums+1)//2`.

# Correctness

`MergeLists` uses the following pointers to locate a pair of adjacent sorted runs:

- `ptrS`: The node before the region being merged.
- `ptr1`, `ptr2`: The first unprocessed nodes in the two sorted runs.
- `ptrE`: The first node after the two sorted runs, saved in advance for reconnection.

The left run has length `length`, and the right run has length `min(length,total)`. The code does not disconnect the sublists beforehand. Instead, it uses `rem1` and `rem2` to limit the number of nodes taken from each run, preventing traversal beyond their respective boundaries.

During merging, the smaller of the two run heads is taken each time. After one run is exhausted, nodes are taken from the other run. Therefore, the merged result remains in ascending order and contains all nodes from both runs. When values are equal, the node from the left run is taken first, so the sort is stable.

After merging, connect the result after `ptrS`, reconnect its tail to `ptrE`, and finally move `ptrS` to the merged tail to continue processing the next pair.

Initially, single-node runs are naturally sorted. Each round preserves sorted order and halves the number of runs. Therefore, when only one run remains, the entire linked list is sorted.

# Complexity

Let the number of nodes be `n`:

- Time complexity: `O(n log n)`. Locating boundaries and merging take a total of `O(n)` time per round, and there are `O(log n)` rounds.
- Space complexity: `O(1)`. The original nodes are reconnected directly, using only a fixed number of pointers and auxiliary nodes, with no recursive call stack.