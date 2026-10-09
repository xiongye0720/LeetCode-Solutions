# Approach

Use one-dimensional dynamic programming. Each state represents the side length of the largest all-`1` square whose bottom-right corner is the current cell.

To reduce space usage, the code chooses the traversal direction based on the matrix dimensions:

- When `m <= n`, traverse column by column. Before the update, `dp[i]` represents the state to the left, while the updated `dp[i-1]` represents the state above.
- When `m > n`, traverse row by row. Before the update, `dp[j]` represents the state above, while the updated `dp[j-1]` represents the state to the left.

The side length in the first row or first column can only be `0` or `1`, so initialize these states directly. For the remaining cells, set the state to `0` when the cell is `'0'`. When the cell is `'1'`, update the state using the states to the left and above.

# Correctness

Let `a` and `b` be the side lengths to the left and above, respectively, and let `s = min(a,b)`. The current side length is at most `s+1`: if it were larger, removing the last column or last row would contradict the maximality of the neighboring states.

When the current cell is `'1'`:

- **`s = 0`**: a square of side length `2` cannot be formed, so the current side length is `1`.
- **`a != b`**: the larger neighboring square has a side length of at least `s+1`. Together with the square of side length `s` on the other side and the current cell, it covers the entire target square. Therefore, the current side length is `s+1`.
- **`a = b = s > 0`**: the two neighboring squares and the current cell cover the target region of side length `s+1`, except for its top-left corner `(i-s, j-s)`. If this corner is `'1'`, the side length increases to `s+1`. Otherwise, it remains `s`, because the bottom-right region of side length `s` still consists entirely of `1`s.

Therefore, each update gives the maximum side length for a square with the current cell as its bottom-right corner. `maxLen` records the maximum across all states, and the code returns `maxLen * maxLen`, which is the maximum area.

# Complexity

- Time complexity: `O(mn)`, since each cell is processed once.
- Space complexity: `O(min(m,n))`, since the dynamic programming array is allocated along the shorter dimension.