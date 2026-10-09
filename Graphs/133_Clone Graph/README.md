# Approach

The code traverses the original graph using BFS. `gNode` stores a mapping from each original node's `id` to its clone and also tracks which nodes have been discovered.

First, create a clone of the starting node and enqueue the original starting node. When processing `temNode`, retrieve its corresponding `cloneN` and iterate over its neighbors:

- If a neighbor has not been recorded, create its clone, save the mapping, and add the original neighbor to `temOps` for processing in the next round.
- Whether or not the neighbor is newly discovered, append its corresponding clone to `cloneN.neighbors` to copy the current adjacency relation.

After traversal, return the clone of the starting node. For an empty input, return `None` directly.

# Correctness

The mapping is saved as soon as each original node is discovered, so each node is cloned and enqueued only once. Even if the graph contains cycles, nodes are not processed repeatedly.

All reachable nodes are traversed, and every adjacency relation connects the corresponding cloned nodes. Therefore, the cloned graph preserves the original graph's node values and connection structure. All nodes and neighbor lists are newly created objects, producing a deep copy.

# Complexity

Let `V` be the number of reachable nodes and `E` be the number of edges.

- **Time complexity:** `O(V+E)`. Each node is processed once, and both directions of each undirected edge are scanned once.
- **Auxiliary space complexity:** `O(V)`. This is used for the mapping and queues. Including the returned cloned graph, the total space complexity is `O(V+E)`.