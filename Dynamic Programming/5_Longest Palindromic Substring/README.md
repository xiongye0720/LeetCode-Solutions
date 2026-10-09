# Approach

Enumerate centers from left to right. `dp[i]` stores both types of palindrome radii:

- `dp[i][0] = r`: the palindrome centered at `i` spans `[i-r+1, i+r-1]` and has length `2r-1`.
- `dp[i][1] = r`: the palindrome centered at `(i-1, i)` spans `[i-r, i+r-1]` and has length `2r`.

`CalRadius` starts from the confirmed radius and compares pairs of outer characters until they do not match or an index goes out of bounds, obtaining the maximum radius for that center.

The code uses `lCenter` and `rCenter` to record the center of the palindrome with the farthest right endpoint, and `rBound` to record that endpoint. This allows previously computed palindrome information to be reused.

# Correctness

When `i > rBound`, there is no covering interval to reuse. The odd-length palindrome starts expanding from radius `1`, and the even-length palindrome starts from radius `0`.

When `i <= rBound`, the current center lies within a known palindrome:

- The mirror position of the odd center `i` is `symPt = lCenter + rCenter - i`.
- The mirror center of the even center `(i-1, i)` is `(symPt, symPt+1)`, so the code reads `dp[symPt+1][1]`.

Characters within the known palindrome are symmetric about its center, so the mirror palindrome provides an initial radius for the current center. However, the reused range cannot extend beyond `rBound`. Therefore, each initial radius is the smaller of the mirror radius and `rBound-i+1`, after which `CalRadius` continues checking the outer characters.

This neither skips unconfirmed characters nor misses any part that can be extended further, so both the odd and even radii are computed correctly for every center.

At the end of each iteration, the code updates the covering interval using the palindrome with the farther right endpoint, and updates `maxStr` using the longer palindrome given by the two radii. All centers are considered, so the final slice produces the globally longest palindromic substring.

# Complexity

Let `n` be the length of the string.

- **Time complexity: `O(n)`.** If the mirror radius does not reach the covering boundary, expansion immediately encounters a mismatch. Otherwise, successful comparisons occur only beyond the old `rBound`. In each iteration, the odd and even expansions account for the same boundary growth at most twice, while `rBound` moves right by only `O(n)` in total. Each call also makes at most one failed comparison. The final slice takes at most `O(n)` time.
- **Space complexity: `O(n)`.** `dp` stores two radii for each position, while the other state uses constant space. The slice for the returned string uses at most `O(n)` space.