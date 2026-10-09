# Approach

When `numRows == 1`, return the original string directly. Otherwise, each complete zigzag cycle has a length of `step = 2*numRows - 2`, and the code collects characters row by row.

Let `r` be the index of the current row:

- First and last rows: the gap between adjacent character indices is always `step`, so execute `i = i + step` each time.
- Middle rows: each cycle contains two characters, one in the vertical part and one in the diagonal part. When `count = c`, each iteration reads the characters at indices `(c-1)*step + r` and `c*step - r` in that order, then updates `i` to `c*step + r` for the next iteration. Stop processing the current row when an index is out of bounds.

At the start of each iteration for a middle row, `i % step == r`, so the two index updates in the code give exactly the positions described above. These positions cover all characters in the current row from left to right. The outer loop then processes the rows from top to bottom, so joining `tar` gives the required result.

# Complexity

Let the string length be `n` and the number of rows be `R`:

- Time complexity: `O(n + R)`. A total of `n` characters are collected, the outer loop still iterates through all `R` rows, and the final join takes `O(n)` time.
- Space complexity: `O(n)`, for the character list and the result string.

When `R == 1`, the string is returned directly, so both the time and extra space are `O(1)`.