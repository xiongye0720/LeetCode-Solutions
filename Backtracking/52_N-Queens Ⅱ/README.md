# Approach

Place queens row by row. `DFS(lvl, pos, ...)` places a queen in row `lvl`, column `pos`, and adds its column and two diagonals to the sets:

- `vert`: the column index `pos`.
- `pd`: the diagonal index `n - lvl + pos`. Positions on the same diagonal have the same column minus row value.
- `nd`: the diagonal index `lvl + pos - 1`. Positions on the same diagonal have the same row plus column value.

Then iterate over all columns in the next row, recursing only when the column and both diagonals are unoccupied.

When `lvl == n`, `n` queens that do not attack each other have been placed, so increase the answer by one. Before each call returns, remove the current queen's occupancy records so that other branches can use those positions.

# Correctness

Each level places exactly one queen in one row, so no two queens share a row. The three sets record the columns and diagonals occupied by previous queens. The checks before recursion rule out all other attacks, so every counted arrangement is valid.

The code explores all columns in the first row and tries all valid positions in each subsequent row, so no valid arrangement is missed. Each arrangement corresponds to a unique sequence of column choices made row by row, so none is counted more than once.

During backtracking, removing the current queen's records restores the sets to their state before entering the current level, ensuring that different branches do not affect each other.

# Complexity

- **Time complexity upper bound: `O(n · n!)`.** Since columns cannot be repeated, the number of search nodes is bounded by the number of column permutations, giving `O(n!)`. Each non-terminal node also iterates over all `n` columns. The diagonal checks further prune the search.
- **Space complexity: `O(n)`.** The recursion depth is `n`, and each of the three sets stores at most `n` elements.