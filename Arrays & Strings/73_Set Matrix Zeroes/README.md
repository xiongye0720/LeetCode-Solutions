# Approach

The first traversal uses the matrix itself to store markers:

- `matrix[i][0] == 0` indicates that row `i` needs to be set to zero, including the first row.
- For `j > 0`, `matrix[0][j] == 0` indicates that column `j` needs to be set to zero.
- `initCol == 0` indicates that the first column of the original matrix contains a zero, so the entire first column needs to be set to zero.

When a zero is found, set the markers for its row and column. Since `matrix[0][0]` records the state of the first row, `initCol` stores the state of the first column separately.

The second traversal proceeds from the bottom-right corner to the top-left corner, setting elements to zero according to the row and column markers. The first column is handled using the row markers and `initCol`.

# Correctness

The first traversal proceeds from top to bottom and from left to right. New markers are written only to positions that have already been visited, so they are not mistaken for original zeros. After the traversal, the markers accurately indicate which rows and columns contain zeros in the original matrix.

The reverse order of the second traversal ensures that markers are not overwritten before they have been fully used:

- The first column is processed last in each row, preserving the row marker for the other elements.
- The first row is processed last, preserving the column markers for the other rows.

Therefore, each element is set to zero exactly when its row or column originally contained a zero.

# Complexity

Let the matrix have `m` rows and `n` columns.

- **Time complexity:** `O(mn)`, since the entire matrix is traversed twice.
- **Extra space complexity:** `O(1)`, since the markers are stored in the original matrix and only a constant number of variables are used.