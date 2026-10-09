# Approach

First, convert `wordList` to a set. If `endWord` is not in the set, return `0` directly.

For each word, replace one position at a time with `'X'` to build a “pattern → word list” mapping. If two distinct words share a pattern, they differ by exactly one character and can be transformed into each other.

Use level-order BFS:

- `ops` stores the words in the current level, and `temOps` collects the next level.
- Use all patterns of the current word to find unvisited words, and add them to `visited` when they are enqueued.
- After scanning a pattern, delete its group to avoid scanning it again later.

`cnt` represents the sequence length at the current level. After expanding this level, if `endWord` has been visited, return the sequence length of the next level, `cnt + 1`.

# Correctness

The pattern groups find all valid one-step transformations from the current word. BFS visits words in increasing order of the number of transformations, so the first visit to `endWord` gives the shortest transformation sequence.

When a pattern is processed for the first time, all unvisited words in its group are enqueued. Using the same pattern again cannot discover new words, so deleting the group neither misses reachable words nor affects the shortest path.

If the queue is exhausted without reaching the end word, no valid transformation sequence exists, so return `0`.

# Complexity

Let `N` be the number of words in the dictionary after removing duplicates, and `L` be the length of each word.

- **Time complexity: `O(NL²)`.** Each word generates `L` patterns, and each slicing, concatenation, and string hashing operation takes `O(L)` time. During BFS, each word is enqueued at most once, and each group is scanned at most once. The total number of entries scanned across all group lists is `O(NL)`.
- **Space complexity: `O(NL²)`.** At most `NL` pattern strings of length `L` are stored. Word references in the groups use `O(NL)` space, while the queues and visited set use `O(N)` space.