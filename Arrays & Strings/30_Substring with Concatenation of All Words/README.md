# Approach

Let the word length be `D`, the number of words be `m`, and the target window length be `mD`. If `s` is too short, return an empty list directly.

First, use `wordIdx` to assign an index to each distinct word, and use `wordDict` to record the required occurrence count for each index. Then preprocess `idx`: for each position in `s`, record the index of the substring of length `D` starting at that position, or `-1` if it is not a target word.

Divide the starting positions into `D` groups by their remainder modulo `D`. In each group, both `left` and `right` move in steps of `D`. Before each check, the window `[left, right)` contains exactly `m` word positions. Fill the window first, then remove one word and add one word in each subsequent iteration.

`temDict` records the occurrence counts of target words in the window, and `diff` records **the number of distinct words whose counts exactly match the requirements**. When adding or removing a word, increase `diff` if its count becomes the required value, and decrease `diff` if its count leaves the required value. When `diff == len(wordDict)`, record the window's starting position.

# Correctness

All words have the same length, so the word boundaries for any valid starting position are spaced `D` characters apart. Traversing all remainder groups covers every candidate starting position.

`temDict` is updated accurately as the window moves, and `diff` always equals the number of distinct words whose counts match the requirements. Therefore, `diff == len(wordDict)` if and only if all target word counts are correct, including repeated words.

Although `-1` is not counted, the window has only `m` word positions, and the required counts of the target words also sum to `m`. When all counts are correct, the target words already fill the window, so it cannot contain any non-target words. Therefore, the condition is both sufficient and necessary.

# Complexity

Let `n=|s|`, and let the number of distinct words be `u`. The following analysis assumes average-case hash table performance.

- **Time complexity:** `O((n+m)D)`. Building the word mapping takes `O(mD)`. When preprocessing `idx`, each string slice and hash computation takes `O(D)`, for a total of `O(nD)`. Window movements across all groups take `O(n)` in total.
- **Space complexity:** `O(n+u)`. `idx` uses `O(n)` space, and the dictionaries use `O(u)` space. The result list uses at most `O(n)` space.