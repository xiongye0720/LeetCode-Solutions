# Approach

The matrix is sorted when flattened row by row, so binary search can be performed directly over the index range `[0, m*n-1]` without actually creating a one-dimensional array.

The one-dimensional index `mid` corresponds to the following matrix position:

- Row index: `mid // n`
- Column index: `mid % n`

The code first handles boundary cases using the first and last elements:

- If the target is less than the first element or greater than the last element, return `False`.
- If the target equals the last element, return `True`.
- In the remaining cases, `first element <= target < last element` holds, so proceed with binary search.

During binary search, update `left` if the middle element is less than or equal to the target; otherwise, update `right`. Once the two indices are adjacent, check whether the element corresponding to `left` equals the target.

# Correctness

Each row of the matrix is increasing, and the first element of the next row is greater than the last element of the previous row. Therefore, the sequence obtained by flattening the matrix row by row is sorted, and the index conversion preserves this order.

The binary search always maintains:

`matrix[left//n][left%n] <= target < matrix[right//n][right%n]`

Each update preserves this relation and narrows the interval. When the search ends, `left` is the last position whose value is less than or equal to the target. If the value at this position does not equal the target, the target does not exist. Therefore, the final check correctly determines whether the target exists.

# Complexity

- **Time complexity: O(log(mn))**.
- **Space complexity: O(1)**, since only index conversion is performed and no additional array is created.