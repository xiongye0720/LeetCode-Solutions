# Approach

The code uses in-place swaps to determine the elements of each permutation one position at a time.

- `lvl` in `DFS` indicates that the `lvl`th position is being determined. On entry, the first `lvl-1` positions have already been fixed.
- Swap `nums[tar]` with `nums[lvl-1]` to fix the current position, then iterate over the remaining indices and recursively determine the next position.
- When `lvl == maxLvl`, the entire permutation has been fixed. Copy the elements one by one into `temAns`, then add it to `ans` so that later changes to `nums` do not affect the saved result.
- Before each call returns, undo its swap so that the next branch starts from the same state. The outer loop enumerates the choices for the first position.

# Correctness

Each level selects an element only from the suffix that has not yet been fixed, so every permutation uses all elements exactly once. Each level explores all remaining choices, so no permutation is missed. The problem guarantees that the elements are distinct, so different choice paths do not generate duplicate permutations.

Recursive calls restore the array before returning, so the current level can use `temNum` to undo its own swap. Thus, the branches do not affect each other.

# Complexity

Let the array length be `n`.

- **Time complexity:** `O(n · n!)`. There are `n!` permutations, and copying each one takes `O(n)` time.
- **Auxiliary space complexity:** `O(n)`, for the recursion stack and the current result copy.
- **Space complexity including the returned results:** `O(n · n!)`.