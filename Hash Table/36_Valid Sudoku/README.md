# Approach

The outer loops `i` and `j` identify the nine boxes, while the inner loops `k` and `l` visit the nine cells in the current box. The actual coordinates are `(i*3+k, j*3+l)`. Empty cells `'.'` are skipped.

For each digit `num`:

- `charDict[num][0]` stores the row indices where it has appeared, and `charDict[num][1]` stores the column indices where it has appeared. If the current row or column index is already present, the digit is repeated in the same row or column, so return `False`; otherwise, add the indices to the records.
- `sqList[num-1]` marks whether it has appeared in the current box. If it is already marked, the digit is repeated within the box, so return `False`. Reinitialize `sqList` when entering each new box.

Return `True` after all checks pass.

# Correctness

`charDict` retains its records throughout the traversal, so any digit that appears again in the same row or column will be detected. `sqList` only retains records for the current box, so it detects exactly the duplicates within that box without including information from other boxes.

Each cell is visited exactly once, and any duplicate will be detected at its later occurrence. If no duplicate check is triggered, all rows, columns, and boxes satisfy the requirements.

# Complexity

- **Time complexity:** `O(1)`. The board has a fixed size of `9 × 9`, so at most 81 cells are checked.
- **Space complexity:** `O(1)`. The number of possible digits, the range of row and column indices, and the length of `sqList` are all fixed.