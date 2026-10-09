# Approach

Reverse the words in the dictionary and insert them into a trie, using `endTag` to mark the end of each word.

`dp[i]` indicates whether the prefix `s[:i]` can be formed from words in the dictionary, with `dp[0] = True`.

For each position `i`, `Check` scans backward from `s[i-1]` while following matching paths down the trie. When it reaches the end of a word and `dp[ptr]` is true, this means:

- `s[ptr:i]` is a word in the dictionary.
- The preceding prefix `s[:ptr]` can be segmented.

Therefore, the entire prefix `s[:i]` can be segmented. If no such split point is found, set `dp[i]` to `False`.

# Correctness

Scanning backward while matching against the trie of reversed words checks all dictionary words ending at position `i`. If a path cannot continue, a longer match is also impossible.

When processing `dp[i]`, all `dp[ptr]` states that might be needed have already been computed. Therefore, each prefix is correctly evaluated as “a segmentable prefix + one dictionary word,” and `dp[-1]` is the final answer.

Although all entries in `dp` are initially `True`, the dictionary words are nonempty, so `ptr < i` must hold whenever the end of a word is reached. Thus, no undetermined state is read.

# Complexity

Let `n` be the length of the string, `D` be the total length of all words in the dictionary, and `L` be the length of the longest word.

- **Time complexity:** `O(D + n·min(n, L))`. Building the trie takes `O(D)` time, and each position matches at most `min(n, L)` characters backward.
- **Space complexity:** `O(D + n)`. The trie uses `O(D)` space, the dynamic programming array uses `O(n)` space, and the recursion stack uses at most `O(L)` space, which is already included in this bound.