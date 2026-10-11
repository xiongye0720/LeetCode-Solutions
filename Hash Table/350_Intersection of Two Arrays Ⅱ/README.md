# Approach

First, use `cnt1` and `cnt2` to count the occurrences of each number in the two arrays. For each number `key` present in both arrays, its frequency in the intersection is `min(cnt1[key],cnt2[key])`. Add it to the corresponding group in `res[freq]`.

Then sort the groups by frequency in ascending order, sort the numbers within each group in ascending order, and finally add each number to `ans` according to its frequency. Therefore, the result is sorted first by frequency in the intersection, then by number when the frequencies are equal.

Each common number is output exactly as many times as the smaller of its occurrence counts in the two arrays. This neither exceeds its count in either array nor leaves out any intersection elements. Sorting only affects the output order and does not change the contents of the intersection.

# Complexity

Let the lengths of the two arrays be `n` and `m`, and let the number of distinct common numbers be `k`.

- **Time Complexity:** `O(n + m + k log k)`. Hash operations are evaluated on average; counting and lookups take `O(n + m)`, and sorting the groups and the numbers within them takes at most `O(k log k)` in total. The result length does not exceed `min(n,m)`.
- **Space Complexity:** `O(n + m)`. This includes the count dictionaries, groups, temporary space for sorting, and the returned list.