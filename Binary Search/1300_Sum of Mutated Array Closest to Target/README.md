# Approach and Correctness

Let `f(v)` be the array sum after replacing all elements greater than `v` with `v`. As `v` increases, `f(v)` is nondecreasing.

If the original array sum satisfies `total ≤ target`, capping cannot bring the array sum closer to the target, so return `maxVal`. It is the smallest cap that keeps the original array sum unchanged.

Otherwise, binary search maintains `f(left) ≤ target < f(right)`. In each round, the code scans the array to calculate `f(mid)` and updates the endpoints based on its comparison with the target, until `right = left + 1`.

At this point, a cap smaller than `left` cannot be closer to the target than `left`, and a cap greater than `right` cannot be closer to the target than `right`. Therefore, only the differences between `lowTotal` and the target and between `highTotal` and the target need to be compared. If the differences are equal, return the smaller value, `left`.

# Complexity

Let `n` be the array length and `M` be the largest element.

- **Time Complexity:** `O(n log(M + 1))`. Each round of binary search scans the entire array. Initialization and the final comparison each require one linear scan.
- **Auxiliary Space Complexity:** `O(1)`. Only a fixed number of variables and fixed-length lists are used, and `nums` directly references the original array.