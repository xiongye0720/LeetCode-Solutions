# Approach and Correctness

The code copies the pairs into `intv`, sorts them by their left endpoints in ascending order, and scans from left to right. After each iteration, `count` is the longest chain length that can be formed from the pairs scanned so far, and `lastIntv[1]` is the smallest ending right endpoint among these longest chains.

If `item[0] > lastIntv[1]`, the current pair can be appended to the chain, increasing its length by `1`. Every chain of the new length must end with the current pair, so the invariant still holds after updating `lastIntv`.

Otherwise, the current pair cannot extend even the longest chain with the smallest ending right endpoint, so the chain length cannot increase. If `item[1] < lastIntv[1]`, the code replaces the last pair in the chain with the current pair. Since the current pair's left endpoint is no smaller than that of the old last pair, it can still follow the preceding pair in the original chain, while giving a smaller ending right endpoint. After the scan, the code returns `count`.

# Complexity

Let `n` be the number of pairs.

- **Time Complexity:** `O(n log n)`. Copying and scanning each take `O(n)`, so sorting dominates.
- **Auxiliary Space Complexity:** `O(n)`. `intv` stores `n` pairs, and sorting also requires `O(n)` temporary space in the worst case.