# Approach

Use the shorter array as the first argument of `cmpParirs`. Fix its index `i` and pair it with each element of the second array in order:

```text
(nums1[i], nums2[0]), (nums1[i], nums2[1]), ...
```

Since the arrays are sorted in ascending order, the pair sums in each sequence are also non-decreasing.

The min-heap stores the first pair that has not yet been output from each sequence, with entries in the form `(pair sum, i, j)`. Each time the smallest pair is popped, push the next pair from the same sequence into the heap. Repeat this `k` times.

`vers` restores the original order of the two elements in each answer pair after the arrays are swapped.

# Correctness

The remaining pairs in each sequence have sums no smaller than its current heap candidate. Therefore, the smallest sum among all pairs that have not yet been output must come from the current candidate of some sequence. Popping the heap top each time generates the answer in ascending order of pair sums.

Initialization keeps only the first `min(k, len(nums1))` sequences. If any sequences are omitted, the first `k` sequences have already been kept. The first pair in each of these sequences has a sum no greater than any pair in the omitted sequences. Therefore, the kept sequences alone are sufficient to select `k` pairs with the smallest sums.

# Complexity

Let the lengths of the two arrays be `m` and `n`, and let the maximum heap size be `h = min(k, m, n)`.

- **Time complexity: `O(k log(h + 1))`.** Initialization inserts `h` elements one by one, followed by `k` pops and at most `k` pushes.
- **Auxiliary space complexity: `O(h)`.** The heap stores at most `h` elements. Including the returned result, the total space complexity is `O(h + k)`.