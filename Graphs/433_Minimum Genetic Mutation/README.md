# Approach

The code uses wildcard grouping and level-order BFS.

Convert `bank` to a set and add the starting gene. For each gene, replace one position at a time with `*`, and use `pattern` to store the corresponding list of genes. If two distinct genes share the same pattern, they differ by exactly one character and can be transformed into each other in one mutation.

`ops` stores the current level, and `temOps` collects the next level. Increment `cnt` before processing each level. Genes are recorded in `visited` when they are enqueued to avoid repeated searches. After scanning a pattern, clear its list to avoid traversing it again.

# Correctness

BFS searches in increasing order of the number of mutations. Therefore, if the ending gene has been visited after processing a level, `cnt` is the minimum number of mutations.

Clearing a pattern's list does not miss any paths: during the first scan, all unvisited genes in the group enter the next level. Scanning the same pattern later cannot discover new genes.

If the starting gene equals the ending gene, return `0`. Otherwise, if the ending gene is not in the gene bank or remains unreachable after the search ends, return `-1`.

# Complexity

Let the input gene bank contain `n` genes, each with a fixed length of 8.

- **Time complexity:** `O(n)`. Each gene is enqueued at most once, and each pattern list is fully scanned at most once. All lists together store `8(n+1)` gene references.
- **Space complexity:** `O(n)`. This is used for the set, wildcard dictionary, visited records, and queues.