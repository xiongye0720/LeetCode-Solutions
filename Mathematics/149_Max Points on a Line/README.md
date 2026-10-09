# Approach

Iterate over each base point `points[i]` and determine a line with each subsequent point `points[j]`:

`Ax + By + C = 0`

The coefficients calculated by the code are:

- `A = yj - yi`
- `B = xi - xj`
- `C = yi*xj - xi*yj`

To give the same line the same dictionary key, the code normalizes the coefficients in two steps:

1. Use `GCD` to find the greatest common divisor of `|A|, |B|, |C|`, and divide all three coefficients by it.
2. Normalize the sign so that the first nonzero coefficient among `A, B` is positive.

Then use the normalized `(A,B,C)` as the key to count subsequent points on the same line. `temMax+1` includes the base point, and `maxQty` stores the global maximum.

# Correctness

The problem guarantees that all points are distinct, so two points determine a unique line, and `A, B` cannot both be zero. Therefore, the greatest common divisor used to reduce the coefficients is always greater than zero.

The coefficient triples for the same line differ only by a nonzero factor. Dividing by the greatest common divisor removes differences in magnitude, and normalizing the sign removes differences in sign. Therefore, the same line has a unique key, and different lines are not merged. All calculations use integers and directly handle horizontal and vertical lines.

Although the code only considers `j > i`, it does not miss the optimal result: for any group of collinear points, choose the point with the smallest index as the base point. All remaining points will be counted under the same key. Therefore, the full number of points in that group is counted, and the global maximum is obtained.

# Complexity

Let the number of points be `n` and the upper bound on the absolute values of the coordinates be `M`, where `M` is at least `2`.

- Time complexity: `O(n² log M)`. A total of `O(n²)` pairs of points are considered. Computing the greatest common divisor for each pair takes `O(log M)`, and dictionary operations take `O(1)` on average. When the coordinate range is fixed by the problem, this can be treated as `O(n²)`.
- Space complexity: `O(n)`. The dictionary for each base point stores at most `n-1` lines and is rebuilt in the next iteration.