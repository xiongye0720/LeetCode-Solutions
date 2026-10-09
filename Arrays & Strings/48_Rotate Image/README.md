# Approach

Process the matrix layer by layer from the outside inward, with `left` and `right` representing the boundaries of the current layer. For each offset `i`, select four corresponding positions:

| Position | Coordinates |
|---|---|
| Top | `(left, left+i)` |
| Right | `(left+i, right)` |
| Bottom | `(right, right-i)` |
| Left | `(right-i, left)` |

The code swaps the top position with the right, bottom, and left positions in that order. If the original values at these four positions are `(A, B, C, D)`, they become `(D, A, B, C)` after the swaps, completing a clockwise rotation.

After processing each layer, increase `left` by one and decrease `right` by one, then continue with the inner layer. For a matrix of odd size, only the center element remains at the end. At this point, `range(right-left)` is empty, so the center stays unchanged.

# Correctness

A 90° clockwise rotation maps position `(r, c)` to `(c, n-1-r)`. Since `left+right == n-1` holds for each layer, the four positions above map in the order top→right→bottom→left→top. The three swaps correctly perform this mapping.

`i` ranges from `0` to `right-left-1`: `i=0` processes the four corners, while the remaining offsets process the interior elements of each edge. Therefore, every element in each layer participates in exactly one group of rotations, with no omissions or repetitions. The layers do not overlap, so the entire matrix is rotated correctly.

# Complexity

- **Time complexity:** `O(n^2)`. Each non-center element participates in a group of a constant number of swaps.
- **Extra space complexity:** `O(1)`. Only a constant number of variables are used, and the original matrix is modified directly.